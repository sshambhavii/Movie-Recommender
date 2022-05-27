import re
import streamlit as st
import pandas as pd
from views import common
movieAPI = '2a3727b4'


@st.cache()
def load_data():
    df = pd.read_json('./Data/top_rated.json',
                      orient='split', compression='infer')
    return df


def working():
    expander = st.expander("Working of top rated page")
    expander.write("Recommends the top 15 IMDB rated movie")
    expander.info("""Uses Weighted Rating by taking 2 parameters:\n
    IMDB Score
    Number of users for each review""")
    expander.image("./assets/images/top_rated.png")


def load_view():
    df = load_data()
    working()
    st.subheader("Top 15 movies ")
    movie_list = []

    for movie in df['movie_title']:
        x = re.sub(r"(\xa0|\362)", "", movie)
        movie_list.append(x)
    common.get_results(movie_list, 3)
