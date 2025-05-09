import pickle
import pandas as pd
import streamlit as st

movies = pickle.load(open('movie_dict.pkl', mode='rb'))
df = pd.DataFrame(movies)
# print(df)

similarity = pickle.load(open('similarity.pkl', mode='rb'))
# print(similarity)


def recommend(movie):
    
    recommended_movies = []

    movie_index = df[df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]    
    
    for i in movie_list:
        recommended_movies.append(df.iloc[i[0]].title)

    return recommended_movies


# print(recommend('Iron Man'))


# Streamlit Web-App

st.title('Movie Recommendation System🎬')
selected_movie = st.selectbox("Select your movie to get recommendations:", list(df['title'].values))
btn = st.button('Recommend')

if btn:
    movies_list = recommend(selected_movie)
    for i in movies_list:
        st.write(i)