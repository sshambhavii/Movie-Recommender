import streamlit as st
import utils as utl
from views import genres, home, hybrid, algorithms_usage, configuration, search, for_you, top_rated

st.set_page_config(layout="wide", page_title='Movie')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "hybrid":
        hybrid.load_view()
    elif route == "genres":
        genres.load_view()
    elif route == "for_you":
        for_you.load_view()
    elif route == "search":
        search.load_view()
    elif route == "top_rated":
        top_rated.load_view()
    elif route == "algorithms_usage":
        algorithms_usage.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()


navigation()
