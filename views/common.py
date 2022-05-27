import streamlit as st
import requests
movieAPI = '2a3727b4'


def grid(list, movie_list, rows=2):
    k = 0
    for i in range(0, rows):
        cols = st.columns(5)
        # first column of the ith row
        cols[0].image(list[i][0], caption=f'{k+1}. {movie_list[k]}')
        k = k+1
        cols[1].image(list[i][1], caption=f'{k+1}. {movie_list[k]}')
        k = k+1
        cols[2].image(list[i][2], caption=f'{k+1}. {movie_list[k]}')
        k = k+1
        cols[3].image(list[i][3], caption=f'{k+1}. {movie_list[k]}')
        k = k+1
        cols[4].image(list[i][4], caption=f'{k+1}. {movie_list[k]}')
        k = k+1


def get_results(movie_list, rows=2):
    r = rows
    k = 0
    list = []
    sublist = []
    for i in range(r):
        for j in range(5):
            movie = movie_list[k]
            url = f"http://www.omdbapi.com/?t={movie}&apikey={movieAPI}"
            try:
                res = requests.get(url)
                res = res.json()
                if res['Poster'] == 'N/A':
                    sublist.append("https://i.ibb.co/tXz6v8K/poster.jpg")
                else:
                    sublist.append(res['Poster'])
            except:
                sublist.append(
                    "https://i.ibb.co/tXz6v8K/poster.jpg")
            k = k+1
        list.append(sublist)
        sublist = []

    grid(list, movie_list, r)
