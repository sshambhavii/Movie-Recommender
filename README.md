# Movie Recommender

This app recommends movies to users based on different user inputs.
It demonstrates 3 types of filterings:
1. Content based Filtering
2. Collaborative Filtering
3. Hybrid Filtering


## Features

- RECOMMENDATIONS BASED ON SEARCH RESULTS 
- GENRE BASED RECOMMENDATIONS
- TOP RATED MOVIES
- PLOT BASED RECOMMENDATIONS
- AGE BASED RECOMMENDATIONS
- COLLABORATIVE FILTERING (MF)
- HYBRID MODEL
- ALGORITHMS USAGE


## Tech Stack

**Frontend:** Streamlit with integrated CSS,JS

**Backend:** Python


## Dataset Used
- MOVIELENS 100K DATASET: [LINK](https://grouplens.org/datasets/movielens/100k/)
- IMDB 5000 MOVIE DATASET : [LINK](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset)

## Installations

- Streamlit
- numpy
- pandas
- json
- jsonpickle
- webbrowser
- base64
- re
- requests
## Run Locally

Download Trained Datasets

- Download the "Data" folder which contains all the pre-processed and trained datasets from the following link.
- Add it to the project's main directory
- Link to the Data folder : [Link](https://drive.google.com/drive/folders/1PTBJiXeEcpoap6qNUJosgW6SR3RuDkQ2?usp=sharing)
- The file structure should look like this 
![File Structure](https://drive.google.com/uc?export=view&id=1JZfW1f0cWVr-NalV0ZazPdHvZ_NfII2C)


Clone the project

```bash
  git clone https://github.com/sshambhavii/Movie-Recommender.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

Start the server
```bash
  streamlit run main.py
```


## App Workflow 

![Flowchart](https://drive.google.com/uc?export=view&id=11G-3ixQ2FSMXhRPKNFie6dsJhipvE5q4)

## Documentation

A presentation giving detailed information about the app and algorithms used is linked 
[here](https://docs.google.com/presentation/d/12k7tk-Zvy5oKH6qfSPgycs02RTbArbdJ/edit?usp=sharing&ouid=113614194640103768865&rtpof=true&sd=true)


## Demo

Video demo for the app here : [Link](https://youtu.be/Rg8yRdG-M58)


## Screenshots

### Home Page
![Home page](https://drive.google.com/uc?export=view&id=1M5Tz3d3bko1H4xKAMfUedNrj7eJ4mVWe)


### For You Page
![For You page](https://drive.google.com/uc?export=view&id=1TCI3aska0_5BnDhBJlFeHuZE0DkkpI60)

### Search Page
![Search page](https://drive.google.com/uc?export=view&id=1F9F1_cfznj-g8LELgTvIOe73FalG6bdh)

### Genre Page
![Genre page](https://drive.google.com/uc?export=view&id=1_ADhcq-Ame_4yIDM8mlh_IDCo7ObG056)

### Top Rated Page
![Top Rated page](https://drive.google.com/uc?export=view&id=1J_xmgV5fgprWoIFxE4lNSAQFa3VKtVdm)

### Hybrid Model
![Hybrid Model page](https://drive.google.com/uc?export=view&id=1TAU_KlkyUbOP4tWYV89C6G2H0YQJcXn8)

## Research Paper Inference

[Link to the paper](https://arxiv.org/pdf/1606.07792.pdf)
