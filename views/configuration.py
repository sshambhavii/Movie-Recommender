import streamlit as st


def load_view():
    col1, col2 = st.columns(2)
    with col1:
        st.expander('Tech Stack and Dataset')
        st.info("""TECH STACK :\n
        FRONTEND : STREAMLIT INTEGRATED WITH HTML, CSS AND JS IN IT
    BACKEND : PYTHON""")
    with col2:
        st.info("""DATASET :\n
        MOVIELENS 100K DATASET
    IMDB 5000 MOVIE DATASET"""
                )
    st.subheader("""Made by:\n
    SHAMBHAVI SINGH\n
    NIT KURUKSHETRA""")
