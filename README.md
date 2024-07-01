# Movie Recommender System

Welcome to the Movie Recommender System. This web application suggests movies based on your selected movie using machine learning techniques and a similarity matrix. The system also fetches movie posters for an enhanced user experience.

## Overview

The Movie Recommender System provides personalized movie recommendations. Users can select a movie from a dropdown list, and the system will recommend similar movies and display their posters.

## Features

- Select a movie from a dropdown list to get recommendations.
- View recommended movies along with their posters.
- Utilizes a cosine similarity matrix for recommendations.
- Fetches movie posters from a local metadata CSV file.

## Requirements

- Python 3.x
- Streamlit
- Pandas
- Numpy
- Scikit-learn
- Pickle

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Anukul03/Movies-Recommendation-System/
    cd movierecommender
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the necessary files:**
    Place `movies.pkl`, `cosine_sim.pkl`, and `movies_metadata.csv` in the `data` directory.

## How to Run

1. **Start the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2. **Open the web browser:**
    The application will be accessible at `http://localhost:8501`.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The Movie Database (TMDb) for providing movie metadata.
- Streamlit for providing an easy-to-use web framework for data science applications.

---

&copy; 2024 Movie Recommender System. All rights reserved.


