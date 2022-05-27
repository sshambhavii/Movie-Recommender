import streamlit as st
import json
import webbrowser
from Algorithms import KNN_Classifier
from views import common


@st.cache()
def load_data():
    with open('./Data/idx_to_movie_sgd.json', 'r+', encoding='utf-8') as f:
        idx_to_movie = json.load(f)


def working():
    expander = st.expander("Working of home page")
    expander.write("User Inputs : ")
    expander.info("Name, Age, Favorite Movie")
    expander.write(
        'Click on "Continue button" to get recommendations based on : ')
    expander.info("User Age")
    expander.info(
        "Collaborative Filtering (User based) - Similar users who like the same movie")
    expander.write("Algorithms used : ")
    expander.info("Classify and sort based on user age")
    expander.info("Stochastic Gradient Descent(SGD)")


def click():
    movie_options = {
        1: "Toy Story",
        2: "Four Rooms",
        3: "Shanghai Triad",
        4: "Stuart Saves His Family",
        5: "Braveheart",
        6: "Clean Slate",
        7: "Twelve Monkeys",
        8: "Dead Man Walking",
        9: "French Twist",
        10: "From Dusk Till Dawn",
    }

    movie_mode = st.sidebar.radio(
        label="Choose a movie option:",
        options=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        format_func=lambda x: movie_options.get(x),
    )
    st.write(f'You have chosen {movie_options.get(movie_mode)}')
    movie = movie_options.get(movie_mode)
    with open('./Data/temp.json', 'w') as outfile:
        json.dump(movie, outfile)


def load_view():
    load_data()
    working()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.image("assets/images/home.jpg")

    with col2:
        user_name = st.text_input("Enter your name ", " ")
        user_age = st.slider('How old are you?', 6, 100, 25)
        with open('./Data/temp_age.json', 'w') as outfile:
            json.dump(user_age, outfile)
        url = 'http://localhost:8501/?nav=for_you'
        st.write("Pick your favourite from the options below: ")
        if st.button('Continue'):
            webbrowser.open_new_tab(url)

    st.title("Pick your favourite")
    movie_list = ['Toy Story', 'Four Rooms', 'Shanghai Triad', 'Stuart Saves His Family',
                  'Braveheart', 'Clean Slate', 'Twelve Monkeys',
                  'Dead Man Walking', 'French Twist', 'From Dusk Till Dawn']
    click()
    common.get_results(movie_list)
