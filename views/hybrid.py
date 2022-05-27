import streamlit as st
import json
import pandas as pd
with open('./Data/hybrid_rating_result.json', 'r+', encoding='utf-8') as f:
    rating_result = json.load(f)

dataset = pd.read_csv('./Data/hybrid_dataset.csv', sep='\t')
result = pd.read_csv('./Data/hybrid_result.csv', sep='\t')


def load_view():
    st.title('Wide & Deep Learning for Recommender Systems')
    expander = st.expander("Working of hybrid model")
    expander.info("""Claim\n
     1.Online experiment results show that Wide & Deep significantly increased app acquisitions compared with wide-only and deep-only models.
     2.It claims to have productionized and evaluated the system on Google Play, a commercial mobile app store with over one billion active
       users and over one million apps.
    """)
    expander.image(
        "https://miro.medium.com/max/1400/1*1jA7Qt71aMK_qG89tfUOoA.png")
    st.info(
        "Link to Research paper [link](https://arxiv.org/pdf/1606.07792.pdf)")
    st.subheader('1. Dataset')
    st.markdown('Input Dataset')
    st.write(dataset.head(5))

    # Taken from the model implementation attacked in Data Folder
    user = 943
    items = 1682
    train_sample = 75000
    test_sample = 25000

    st.write('Users in Dataset after pre-processing')
    st.info(user)
    st.write('Items in Dataset after pre-processing')
    st.info(items)

    st.subheader('2. Feature Specs')
    st.write(
        """Wide feature specs:\n
	    VocabularyListCategoricalColumn(key='userID', vocabulary_list=(196, 63, 226, 154, 306, 296, 34, 271, ...\n
	    VocabularyListCategoricalColumn(key='itemID', vocabulary_list=(242, 302, 377, 51, 346, 474, 265, 465 ...\n
	    CrossedColumn(keys=(VocabularyListCategoricalColumn(key='userID', vocabulary_list=(196, 63, 226, 154 ...\n""")
    st.write("""Deep feature specs:\n
        EmbeddingColumn(categorical_column=VocabularyListCategoricalColumn(key='userID', vocabulary_list=(19 ...\n
        EmbeddingColumn(categorical_column=VocabularyListCategoricalColumn(key='itemID', vocabulary_list=(24 ...\n
        NumericColumn(key='genre', shape=(19,), default_value=None, dtype=tf.float32, normalizer_fn=None) ...\n""")

    st.write('Training Sample')
    st.info(train_sample)
    st.write('Testing Sample')
    st.info(test_sample)

    st.subheader('3. Result Dataset')
    st.write(result.head(5))

    st.header('4. Performance')
    st.write(rating_result)
