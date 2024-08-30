# BingeWhiz-Content-Based-Recommender-System
1) This movie recommender system works on the concept of Cosine Similarity to recommend the top 5 movies based on the user's choice.
2) The several steps involved are:
  - Feature Selection: Selecting which columns in the dataset are relevant for movie recommendation
  -  Data Cleaning: Cleaning the data for the selected features by removing the null values.
  -  Data Processing: Processing the columns of data, merging the data of the relevant columns. Several algorithms like stemming have been used to get hold of the base word and removing the redundant data
  -  Vectorization: In this step we are converting these merged columns into vectors to finally apply Cosine Similarity to get hold of the top 5 closest vectors that will be given to the user as recommendations.
  -  Streamlit Front-end and Connection to the TMDB API: We built a UI where user can type the Movie for which they are looking for 5 best recommendations. We are fetching the data for the website using the TMDB API.  
