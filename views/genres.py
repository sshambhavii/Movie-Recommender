import streamlit as st
import json
from Algorithms import KNN_Classifier
import requests

movieApi = '2a3727b4'


@st.cache()
def load_data():
    with open('./Data/movie_data.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
    with open('./Data/movie_titles.json', 'r+', encoding='utf-8') as f:
        movie_titles = json.load(f)
    return data, movie_titles


def working():
    expander = st.expander("Working of genres page")
    expander.write("User Input : ")
    expander.info("""Three inputs are\n
    Multiple Genres can be selected
    Number of Movies to be recommended
    Threshold IMDB rating for filtering""")
    expander.write("Outputs : ")
    expander.info(
        "Movies recommended based on genre and results sorted in decreasing ratings")
    expander.write("Algorithm used : ")
    expander.info("""K-Nearest Neighbor Algorithm\n
    Does Item based collaborative filtering
    When KNN makes inference about a movie, KNN will calculate the “distance” between the target movie and every other movie in its database, 
    then it ranks its distances and returns the top K nearest neighbor movies as the most similar movie recommendations.
    """)


def KNN_Movie_Recommender(test_point, k):
    data, movie_titles = load_data()
    # Create dummy target variable for the KNN Classifier
    target = [0 for item in movie_titles]
    # Instantiate object for the Classifier
    model = KNN_Classifier.KNearestNeighbours(data, target, test_point, k=k)
    # Run the algorithm
    model.fit()
    # Print list of 10 recommendations < Change value of k for a different number >
    table = []
    for i in model.indices:
        # Returns back movie title and imdb link
        table.append([movie_titles[i][0], movie_titles[i][2], data[i][-1]])
    return table


def run(no_of_reco):
    # st.image(img1, use_column_width=False)
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
              'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']
    sel_gen = st.multiselect('Select Genres:', genres)
    if sel_gen:
        imdb_score = st.slider('Choose IMDb score:', 1, 10, 8)
        test_point = [1 if genre in sel_gen else 0 for genre in genres]
        test_point.append(imdb_score)
        table = KNN_Movie_Recommender(test_point, no_of_reco)
        sorted_table = sorted(table, key=lambda x: x[2], reverse=True)
        return sorted_table

# This page cannot use the the grid function from common module as it takes additional parameters.


def grid(list, movie_list, x, no_of_reco):
    k = 0
    for i in range(0, x):

        cols = st.columns(5)
        # first column of the ith row
        cols[0].image(
            list[i][0], caption=f'{movie_list[k][0]} IMDB Rating : {movie_list[k][1]}')
        if(k+1 == no_of_reco):
            break
        else:
            k = k+1
        cols[1].image(
            list[i][1], caption=f'{movie_list[k][0]} IMDB Rating : {movie_list[k][1]}')
        if(k+1 == no_of_reco):
            break
        else:
            k = k+1
        cols[2].image(
            list[i][2], caption=f'{movie_list[k][0]} IMDB Rating : {movie_list[k][1]}')
        if(k+1 == no_of_reco):
            break
        else:
            k = k+1
        cols[3].image(
            list[i][3], caption=f'{movie_list[k][0]} IMDB Rating : {movie_list[k][1]}')
        if(k + 1 == no_of_reco):
            break
        else:
            k = k+1
        cols[4].image(
            list[i][4], caption=f'{movie_list[k][0]} IMDB Rating : {movie_list[k][1]}')
        if(k + 1 == no_of_reco):
            break
        else:
            k = k+1


def result(no_of_reco, sorted_table):
    st.success(
        'Some of the movies from our Recommendation, have a look below')
    k = 0
    movie_list = []
    for movie, link, ratings in sorted_table:
        temp = []
        temp.append(movie)
        temp.append(ratings)
        movie_list.append(temp)
    list = []
    sublist = []
    x = no_of_reco//5+1

    for i in range(x):
        for j in range(5):
            if(k == no_of_reco):
                break
            movie = movie_list[k][0]
            url = f"http://www.omdbapi.com/?t={movie}&apikey={movieApi}"
            try:
                res = requests.get(url)
                res = res.json()
                if res['Poster'] == 'N/A':
                    sublist.append(
                        "https://i.ibb.co/tXz6v8K/poster.jpg")
                else:
                    sublist.append(res['Poster'])
            except:
                sublist.append(
                    "https://i.ibb.co/tXz6v8K/poster.jpg")
            k = k+1
        list.append(sublist)
        sublist = []

    grid(list, movie_list, x, no_of_reco)


def load_view():
    working()
    st.title('Choose your favourite Genre')

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/images/genre.jpg")

    with col2:
        no_of_reco = st.number_input(
            'Number of movies:', min_value=5, max_value=20, step=1)
        sorted_table = run(no_of_reco)
    if sorted_table:
        result(no_of_reco, sorted_table)
