import streamlit as st
import pickle
import scikit-learn as sk
import numpy as np
import pandas as pd

#Load the Saved Model
with open("movie_recommender.sav", 'rb') as file:
    model=pickle.load(file)

with open("movie_title.sav", 'rb') as file:
    title_df=pickle.load(file)

def recommend_movies(model, features, Movie_Title):
    features_array = np.array(features)
    single_sample = features_array.reshape(1,-1)
    distance,movie_index=model.kneighbors(single_sample)
    recommendations=[]
    for i, index in enumerate(movie_index[0]):
        recommendation_title = title_df.iloc[index]
        if recommendation_title != Movie_Title:
            recommendations.append(recommendation_title)
    return recommendations
    

# Streamlit App

def main():
    st.title("kNN Movie Predictor")
    st.write("Enter the details of a movie that you have enjoyed watching:")


    #Input Fields
    Movie_Title=st.text_input("Movie Name")
    IMDB_Rating=st.number_input("IMDB Rating", min_value=0.0, max_value=10.0, step=0.1, value=5.0)
    Biography = st.radio("Biography", ("Yes", "No"), key="bio_radio")
    Drama = st.radio("Drama", ("Yes", "No"), key="drama_radio")
    Thriller = st.radio("Thriller", ("Yes", "No"), key="thrill_radio")
    Comedy = st.radio("Comedy", ("Yes", "No"), key="comedy_radio")
    Crime = st.radio("Crime", ("Yes", "No"), key="crime_radio")
    Mystery = st.radio("Mystery", ("Yes", "No"), key="mystery_radio")
    History = st.radio("Biography", ("Yes", "No"), key="history_radio")

    #Change Categorical Fields to Numeric Values
    Biography_numeric = 1 if Biography == "Yes" else 0
    Drama_numeric= 1 if Drama == "Yes" else 0
    Thriller_numeric= 1 if Thriller == "Yes" else 0
    Comedy_numeric= 1 if Comedy == "Yes" else 0
    Crime_numeric= 1 if Crime == "Yes" else 0
    Mystery_numeric= 1 if Mystery == "Yes" else 0
    History_numeric= 1 if History == "Yes" else 0

    #Prepare Features for kNN Model Recommendation
    features=[IMDB_Rating, Biography_numeric,Drama_numeric,Thriller_numeric,Comedy_numeric,Crime_numeric,Mystery_numeric,History_numeric]
    

    if st.button("Show Me Recommendations"):
        result=recommend_movies(model, features, Movie_Title)
        st.write(f"Since you enjoyed {Movie_Title}, I would recommend: {result}")

if __name__ == "__main__":
    main()
