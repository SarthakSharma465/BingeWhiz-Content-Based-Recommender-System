import streamlit as st
import pickle
import pandas as pd
import requests

# --- Fetch function ---
def fetch_poster(movie_id):

    ## --- Copied from the API Page ---
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjODk2OTIzMmJmNGIzZTk0NTdlYjczYjkzZDRjZjA2MiIsInN1YiI6IjY0YWZmMjBmYzQ5MDQ4MDBlMjQzMTMxYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5eKiaXWR3OnCG2p1hfAfOvhAE88mLpDuDBXouomBngg"}
    response = requests.get(url.format(movie_id), headers=headers)

    data = response.json()

    # But this is not the complete path so we need to add something more
    # We figured out the additional part from the web -> Tmdb image path

    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']

# --- Recommend function ---
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,  recommended_movies_posters

# --- Loading pickle files ---
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# --- Customization / Design ---
st.set_page_config(layout="wide")
# with open("Design.css") as source_des:
#     st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html= True)

# st.image("https://unsplash.com/photos/anHpletc5s4")
st.title('Binge Whiz')
st.subheader('Content Based Movie Recommender System')
st.divider()



# Now we need the dropdown to show all the movies as the options


selected_movie_name = st.selectbox('Out of movies? Try this out', movies['title'].values)

# --- Button ---
if st.button('Find Recommendations'):
   names, posters = recommend(selected_movie_name)

   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
        st.image(posters[0])
        st.subheader(names[0])
   with col2:
       st.image(posters[1])
       st.subheader(names[1])
   with col3:
        st.image(posters[2])
        st.subheader(names[2])
   with col4:
       st.image(posters[3])
       st.subheader(names[3])
   with col5:
       st.image(posters[4])
       st.subheader(names[4])