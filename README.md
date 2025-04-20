# BSAN_6070_CA07_Streamlit_Based_Cloud_Deployment_of_kNN_based_Movie_Recommender_App

## Description

### This code is utilizing data that can be used to help identify similar movies. Based on certain binary categorical variables (ie. genre classifications) and IMDB score of the movies, this code will be using the kNN (k Nearest Neighbors) model to find the top 5 movies that are similar to the another movie that the user is watching. The data will be trained without the classifying label column because we are not asking the model to classify the movie. Since kNN models can only use numerical data to help determine the relationship between the data points, the data will be separated into numerical and nominal data and then the numerical data will be used to determine the 5 nearest neighbors to the movie of interest once the model is fitted around the movie the user is watching.  

### Once the code from the Colab file (.ipynb file) was finished running, it produced pickle files which saved the cleaning and training processes of the data which produces the kNN model that we are trying to achieve in a deployable application. The two pickle files that this program produces will be the actual training model that will determine the recommeded movies and the other one is the titles of the movies that will match with the indicies of the recommended movies. 

### These two pickle files will then be used in a python file in order to make this predictor deployable on any device with access to the internet regardless of the files being locally installed. This python file will allow the user to input the necessary values for the model to be executed when it is being deployed. Based on the inputs that user contributes, the model will return 5 movies (or 4 if there is a duplicate already in the dataset). 

## Necessary Libraries and Versions

* Numpy (Version 2.0.2)
* Pandas (Version 2.2.2)
* Scikit Learn (Version 1.6.1)
* NearestNeighbors (function from Scikit Learn Neighbors library) (Version 1.6.1)
* Python (Version 3.13.3)
* Pickle (which is a part of Scikit Learn)
* Streamlit (Version 1.44.1

## Data Set and the Source

### The data set is an excel sheet with movies and binary classifying information (mainly genre) and numerical data (IMDB score) that is all compiled in one place. This data set was provided by Professor Arin Brahma that he found on the UCI Machine Learning Repository. You can find the dataset either on this GitHub repository with movie_recommendation_data.csv or you can link it online at ([https://github.com/ArinB/MSBA-CA-03-Decision-Trees/blob/master/census_data.csv?raw=true](https://github.com/ArinB/MSBA-CA-Data/raw/main/CA05/movies_recommendation_data.csv)). 

## Source Code Acknowledgement

### While the code may not be exactly the same, the code in the colab file (.ipynb file) is derrived from the code that I wrote in my original kNN movie recommender repository (https://github.com/ysasson-portfolio/BSAN_6070_CA05_kNN_Recommender/tree/main). It was modified in this case in order to be able to deploy it using streamlit.

## Software Being Used

### Google CoLab
### Microsoft Visual Code Studio
### Streamlit.io
### Text Editor


## Installation

### In order to run this code you need to make sure the following:
* You have internet connection if you plan on getting the data from the direct link to Professor Brahma's GitHub
* If you are planning on doing it on Jupyter Notebook or Google Colab through a direct file, download the movie_recommendation_data.csv file and access it by using the right directory when using the read_csv function.
* Make sure that all necessary packages and libraries are installed locally.
* Make sure that the requirements.txt file is updated with the most current versions of the software (if there is an issue).
* When testing the python code by deploying it locally, make sure that you have all of the files saved in one folder.
* When deploying the python code locally, make sure that you change the directory in your command prompt to the folder where all the necessary .sav files, .py files, and the requirements.txt file are saved.
* The command to testing it locally in your command prompt is streamlit run movie_recommender_knn_app.py
* When deploying the application on streamlit.io, make sure you have all of the necessary files in a Github repository. 
