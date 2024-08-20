import streamlit as st
import pickle
import pandas as pd
import requests

# Load the data
movies_df = pickle.load(open('Movies-Recommender-System.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Fetching Poster Function
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cb408eaa7c1494e61210ab69137fa60e&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']
# Function to recommend movies
def recommend(movie):
    if movie in movies_df['title'].values:
        movie_index = movies_df[movies_df['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_lst = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []
        for i in movies_lst:
            movie_id = movies_df.iloc[i[0]].movie_id
            # fetch poster

            recommended_movies.append(movies_df.iloc[i[0]].title)
            # fetch poster from api
            recommended_movies_posters.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movies_posters
    else:
        return [f"Movie '{movie}' not found, please type the correct name or full name of the movie."]

# List of movie titles for the dropdown
movies_list = movies_df['title'].values

# Streamlit UI
st.title('Movies Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations', movies_list
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])