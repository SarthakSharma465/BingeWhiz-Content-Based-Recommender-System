# BingeWhiz: Content-Based Movie Recommender System

BingeWhiz is a content-based movie recommender system that suggests movies based on a user's preference by leveraging the power of **Cosine Similarity**. The system recommends the top 5 movies similar to the one selected by the user, using data processing techniques and a user-friendly interface built with **Streamlit**.

## Project Overview

BingeWhiz is designed to enhance the movie-watching experience by providing personalized movie recommendations. This system uses a content-based filtering approach, which focuses on the content of the movies themselves rather than user behavior or ratings.

### Key Features:
- **Content-Based Recommendations**: Uses Cosine Similarity to compare the content of movies and suggest similar ones.
- **Data Preprocessing and Cleaning**: Ensures the dataset is clean and ready for analysis.
- **Vectorization**: Converts movie content into vectors for similarity calculation.
- **Streamlit UI**: Provides a simple and interactive interface for users to input their movie of choice.
- **TMDB API Integration**: Fetches additional movie data from The Movie Database (TMDB) to enhance recommendations.

## Project Workflow

The workflow of the BingeWhiz system involves several critical steps:

### 1. Feature Selection
   - **Objective**: Identify the relevant features (e.g., genres, cast, keywords, etc.) from the dataset that contribute to making accurate movie recommendations.
   - **Implementation**: Selected features from the dataset (`tmdb_5000_movies.csv`) that are crucial for determining movie similarity.

### 2. Data Cleaning
   - **Objective**: Clean the dataset by handling missing or null values, ensuring the data is consistent and usable.
   - **Implementation**: Removed null values and handled any inconsistencies to ensure the dataset is ready for processing.

### 3. Data Processing
   - **Objective**: Process the selected features to prepare them for vectorization. This involves text preprocessing steps such as stemming and removing redundant data.
   - **Implementation**: 
     - **Merging Columns**: Combined relevant columns to create a single text-based feature representing the movie.
     - **Stemming**: Applied stemming algorithms to reduce words to their base forms, minimizing redundancy.

### 4. Vectorization
   - **Objective**: Convert the processed textual data into numerical vectors that can be used for similarity calculation.
   - **Implementation**: 
     - Used **TF-IDF Vectorization** to transform the text data into vectors.
     - Applied **Cosine Similarity** to compare these vectors and identify the top 5 most similar movies.

### 5. Building the Streamlit Interface
   - **Objective**: Create an interactive front-end using Streamlit where users can input a movie name and receive recommendations.
   - **Implementation**: 
     - Developed a user-friendly UI with Streamlit.
     - Integrated with the TMDB API to fetch movie data and display additional information about the recommended movies.

### 6. TMDB API Integration
   - **Objective**: Enhance the movie recommendations by fetching detailed information from the TMDB API.
   - **Implementation**: Used the TMDB API to retrieve movie posters, overviews, and other relevant details to enrich the recommendation experience.

## Deployment Status

The BingeWhiz system was intended to be deployed for public use. However, deployment was not completed due to certain restrictions. The project remains in its local development state, but the code and methodology are fully documented for future deployment efforts.

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/BingeWhiz-Content-Based-Recommender-System.git
   cd BingeWhiz-Content-Based-Recommender-System
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run Main.ipynb
   ```

4. **Use the interface**:
   - Enter the name of a movie in the text box.
   - Click "Generate" to receive the top 5 movie recommendations.

## Future Improvements

- **Deployment**: Resolve the existing restrictions to deploy the system online.
- **Enhanced Filtering**: Incorporate additional filters (e.g., release date, rating) to refine recommendations.
- **Collaborative Filtering**: Integrate collaborative filtering techniques to combine content-based and user behavior approaches for improved accuracy.

## Acknowledgments

- **The Movie Database (TMDB)**: For providing the API used to fetch additional movie details.
- **Streamlit**: For enabling the creation of a simple and effective user interface.

## Conclusion

BingeWhiz provides a solid foundation for a personalized movie recommendation system. Despite the deployment challenges, the system effectively demonstrates the use of content-based filtering, offering an engaging experience for movie enthusiasts.

---

This improved README provides a comprehensive overview of your project, detailing the methodology, tools, and future improvements.
