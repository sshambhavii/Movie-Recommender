import streamlit as st
import requests
import base64
import pandas as pd
import pickle
from views import common
movieAPI = '2a3727b4'


@st.cache()
def load_data():
    cos_sim_tfidf = pickle.load(open("./Data/tfidf.pickle", "rb"))
    cos_sim_cv = pickle.load(open("./Data/cv.pickle", "rb"))
    reverse_map = pd.read_json('./Data/reverse_map_cast_plot.json',
                               orient='split', compression='infer')
    data = pd.read_json('./Data/data_cast_plot.json',
                        orient='split', compression='infer')
    return cos_sim_tfidf, cos_sim_cv, reverse_map, data


def working():
    expander = st.expander("Working of search page")
    expander.write("User Inputs : ")
    expander.info("Title of a movie to be searched")
    expander.write(
        'Output')
    expander.info("Gets movie information from OMDB API")
    expander.info("Movies based on similar Cast and Crew")
    expander.info(
        'If user clickes on "Read More", gets movie recommendations based on similar plot')
    expander.write("Algorithms used : ")
    expander.info("""Cast and Crew : Count Vectorizer\n
    Converts text into numerical data by considering frequency of words and then finds similarity.""")
    expander.info("""Plot : TF-IDF Vectorizer\n
    It not only focuses on the frequency of words present in the corpus but also provides the importance of the words.
    We can then remove the words that are less important for analysis, hence making the model building less complex by reducing the input dimensions.""")


def display(result):
    movie_list = []
    for movie in result:
        movie_list.append(movie)
    common.get_results(movie_list)


def get_recommendations(title, cosine_sim):
    cos_sim_tfidf, cos_sim_cv, reverse_map, data = load_data()
    # Get the index of the movie that matches the title
    idx = int(reverse_map[reverse_map['movie_title'] == title].index[0])
    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    # Return the top 10 most similar movies
    return data['movie_title'].iloc[movie_indices]


def get_info(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={movieAPI}"
    re = requests.get(url)
    re = re.json()
    return re


def load_view():
    cos_sim_tfidf, cos_sim_cv, reverse_map, data = load_data()
    working()
    flag = False
    with open("assets/images/home.jpg", "rb") as image_file:
        image_as_base64 = base64.b64encode(image_file.read())
    title = st.text_input("Search your movie")
    if title:
        try:
            re = get_info(title)
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(re['Poster'])
            with col2:
                st.subheader(re['Title'])
                st.caption(f"Genre : {re['Genre']} Year : {re['Year']}")
                st.text(f"Rating : {re['imdbRating']}")
                st.progress(float(re['imdbRating'])/10)
                result = st.button('Read More')
                if result:
                    flag = True
                    st.write(re['Plot'])
        except:
            st.error('No movie with that title')
        st.title(f'More from the cast and crew of {title}:')
        try:
            result = get_recommendations(title, cos_sim_cv)
            display(result)
        except:
            st.write(
                "OOPs the dataset doesnt contain this movie. Try another movie maybe Stuart Little? :(")
        if flag:
            st.title(f'More like the plot of {title}:')
            try:
                result2 = get_recommendations(title, cos_sim_tfidf)
                display(result2)
            except:
                st.write(
                    "OOPs the dataset doesnt contain this movie. Try another movie maybe Stuart Little? :(")
