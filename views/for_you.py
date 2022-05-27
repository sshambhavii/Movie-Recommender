from click import command
import streamlit as st
import jsonpickle
import numpy as np
import json
from views import common
from Algorithms import user_age

movieAPI = '2a3727b4'


@st.cache()
def load_data():
    with open('./Data/sgd_sim.json', 'r+', encoding='utf-8') as f:
        sgd_sim = json.load(f)
    with open('./Data/idx_to_movie_sgd.json', 'r+', encoding='utf-8') as f:
        idx_to_movie = json.load(f)

    decoded_sgd = jsonpickle.decode(sgd_sim)
    return idx_to_movie, decoded_sgd


def working():
    expander = st.expander("Working of for you page")
    expander.write(
        'Recommendations based on : ')
    expander.info(
        "Collaborative Filtering-Similar users who like the same movie")
    expander.info("User Age")
    expander.write("Algorithms used : ")
    expander.info("Classify and sort based on user age")
    expander.info("""Stochastic Gradient Descent(SGD)\n
    Matrix Factorization based on Stochastic Gradient Descent (MF-SGD for short) is an algorithm widely used in recommender systems.
    SGD randomly picks one data point from the whole data set at each iteration to reduce the computations enormously.""")


def display_top_k_movies(similarity, mapper, movie_idx, k=10):
    movie_indices = np.argsort(similarity[movie_idx, :])[::-1]
    # Start i at 1 to not grab the input movie
    k_ctr = 0
    i = 1
    movie = []
    while k_ctr < 10:
        movie.append(mapper[str(movie_indices[i])])
        k_ctr += 1
        i += 1
    return movie


def getmovie():
    idx_to_movie, decoded_sgd = load_data()
    with open('./Data/temp.json', 'r+', encoding='utf-8') as f:
        clicked_movie = json.load(f)
    st.subheader(f"Users who like {clicked_movie} also like : ")
    clean_d = {k: v.rsplit("(")[0].rsplit(",")[0].strip()
               for k, v in idx_to_movie.items()}
    key_list = list(clean_d.keys())
    val_list = list(clean_d.values())
    position = val_list.index(clicked_movie)
    return key_list[position]


def load_view():
    idx_to_movie, decoded_sgd = load_data()
    working()
    idx = int(getmovie())
    res = display_top_k_movies(decoded_sgd, idx_to_movie, idx)
    movie_list = []
    for idx, r in enumerate(res):
        movie_list.append(r.rsplit("(")[0].rsplit(",")[0].strip())
    common.get_results(movie_list)
    st.subheader("People around your age also like: ")
    with open('./Data/temp_age.json', 'r+', encoding='utf-8') as f:
        age = json.load(f)
    movie_list = user_age.age_recom(age)
    common.get_results(movie_list)
