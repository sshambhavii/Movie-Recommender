import streamlit as st


def load_view():
    st.subheader(
        "Link to presentation : [link](https://docs.google.com/presentation/d/12k7tk-Zvy5oKH6qfSPgycs02RTbArbdJ/edit?usp=sharing&ouid=113614194640103768865&rtpof=true&sd=true)")
    st.header("CONTENT BASED FILTERING")
    ex1 = st.expander("TF-IDF VECTORIZER")
    ex1.image("./assets/images/1.png")
    ex2 = st.expander("COUNT VECTORIZER")
    ex2.image("./assets/images/2.png")
    ex3 = st.expander("WEIGHTED MEAN")
    ex3.image("./assets/images/3.png")
    st.header("COLLABORATIVE FILTERING")
    ex1 = st.expander("KNN - ITEM ITEM SIMILARITY")
    ex1.image("./assets/images/4.png")
    ex2 = st.expander("STOCHASTIC GRADIENT DESCENT")
    ex2.image("./assets/images/5.png")
    ex3 = st.expander("USER USER SIMILARITY")
    ex3.image("./assets/images/6.png")
    st.header("HYBRID FILTERING")
    ex3 = st.expander("WIDE AND DEEP MODEL")
    ex3.image("./assets/images/7.png")
    st.header("THE BEST ALGORTIHM?")
    ex = st.expander("Which is the best algorithm ?")
    ex.info("""Hybdrid Approaches?\n
    Most recommendation engines use hybrid algorithms made of many algorithms.
    There are several studies that compare the performance of the conventional approaches with the hybrid methods and say that by using the hybrid
    methods we can generate more accurate recommendations.
    The most modern approaches in recommendation engine algorithm leverage deep learning to combine both collaborative filtering and content-based models""")
    ex.info("""The recommendation algorithm depends on a number of factor like :\n 
    It depends on your evaluation criteria.
    In case you are using implicit feedbacks, it will depend on your feature engineering
    In case your data is distributed uniformly or skewed, one algorithm may outperform others.
    It also depends on the methods you are using. If it is a probabilistic approach or graph approach or X approach.
    It also depends on your computational framework.""")
    ex.info("""SGD > Other algorithms for Collaborative Filtering?\n
    SGD as it seems to be generally faster and more accurate than ALS. As an added bonus, SGDis widely used for training Deep Neural Networks.
    Thus, many high-quality implementations exist for this algorithm.""")
