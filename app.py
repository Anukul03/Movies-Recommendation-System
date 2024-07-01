import streamlit as st
import pickle
import pandas as pd

# Load the metadata CSV file
metadata_df = pd.read_csv("data/movies_metadata.csv")
metadata_df = metadata_df[['id', 'title', 'poster_path']]
metadata_df['id'] = metadata_df['id'].astype(str)  # Ensure IDs are strings

def fetch_poster(movie_id):
    try:
        poster_path = metadata_df[metadata_df['id'] == str(movie_id)]['poster_path'].values[0]
        poster_url = f"https://image.tmdb.org/t/p/w185{poster_path}"
        # Debugging information
        print(f"Movie ID: {movie_id}, Poster Path: {poster_path}, Poster URL: {poster_url}")
        return poster_url
    except IndexError:
        print(f"Poster not found for movie ID: {movie_id}")
        return "Poster not found"

def recommend_movies(movie_name):
    movie_idx = movies_df[movies_df['title'] == movie_name].index[0]
    similarity_scores = similarity[movie_idx]
    similar_movies_indices = similarity_scores.argsort()[::-1][1:10]

    recommended_movies = []
    recommended_movies_poster = []

    for idx in similar_movies_indices:
        movie = movies_df.iloc[idx]['title']
        movie_id = movies_df.iloc[idx]['id']  # Ensure you are getting the correct ID
        recommended_movies.append(movie)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster

# Load data
movies_df = pickle.load(open("movies.pkl", "rb"))
movies_list = movies_df['title'].values
similarity = pickle.load(open("cosine_sim.pkl", "rb"))

st.title("Movies Recommender System")

selected_movie_name = st.selectbox("Select a movie", movies_list)

if st.button("Recommend"):
    st.write(f"Recommended movies for '{selected_movie_name}' are:")
    names, posters = recommend_movies(selected_movie_name)

    rows = 3
    cols_per_row = 3
    for row in range(rows):
        cols = st.columns(cols_per_row)
        for col_idx, col in enumerate(cols):
            index = row * cols_per_row + col_idx
            if index < len(names):
                with col:
                    st.header(names[index])
                    st.image(posters[index])
