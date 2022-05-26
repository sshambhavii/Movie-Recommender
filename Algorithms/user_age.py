import json
import numpy as np
import pandas as pd
np.random.seed(0)

df = pd.read_csv('./Data/ml-100k/u.user', sep='\t', header=None)
new_df = pd.DataFrame([], columns=['user_id', 'user_age',
                      'gender', 'occupation', 'postal_code'])

with open('./Data/idx_to_movie_sgd.json', 'r+', encoding='utf-8') as f:
    idx_to_movie = json.load(f)

for _, row in df.iterrows():
    id, age, gender, job, zipcode = map(lambda x: int(
        x) if x.isdigit() else x, row[0].strip().split('|'))
    if isinstance(zipcode, str):
        continue
    new_df = new_df.append(
        {
            'user_id': id,
            'user_age': age,
            'gender': gender,
            'occupation': job,
            'postal_code': zipcode
        },
        ignore_index=True
    )

names = ['user_id', 'movie_id', 'rating', 'timestamp']
df = pd.read_csv('./Data/ml-100k/u.data', sep='\t', header=None, names=names)
df2 = df[['user_id', 'movie_id', 'rating']]
df2 = df2[df2['rating'] > 3.5]

x = df2['movie_id'].value_counts().mean()
x = df2['movie_id'].value_counts() > 50
y = x[x].index
df2 = df2[df2['movie_id'].isin(y)]

new = df2.merge(new_df, on='user_id')
z = new['user_age'].value_counts()

new = new[["user_id", "movie_id", "user_age", "rating"]]


def get_count(tp, id):
    playcount_groupbyid = tp[[id]].groupby(id, as_index=False)
    count = playcount_groupbyid.size()
    return count


itemcount = get_count(new, 'movie_id')
itemcount = itemcount[itemcount['size'] >= 50]
new = new.drop(['user_id'], axis=1)
new = new.merge(itemcount, on='movie_id')
new = new.drop(['size'], axis=1)
new.sort_values("user_age", inplace=True)


def findage(age):
    if(age < 10 and age > 7):
        new_age = [7, 10]
    if(age < 7):
        new_age = 7
    if(age == 12):
        new_age = [11, 13]
    if(age == 67):
        new_age = [66, 68]
    if(age > 70 and age < 73):
        new_age = [70, 73]
    if(age > 73):
        new_age = 73
    return new_age


def age_recom(new_age):
    if new_age in new['user_age'].values:
        filtered_age = new[new["user_age"] == new_age]
        filtered_age.sort_values(["rating"], inplace=True, ascending=False)
        filtered_age.drop_duplicates(subset="movie_id",
                                     keep=False, inplace=True)
        result = filtered_age.head(10)
    else:
        l = findage(new_age)
        filtered_age1 = new[new["user_age"] == l[0]]
        filtered_age2 = new[new["user_age"] == l[1]]
        filtered_age = pd.concat(
            [filtered_age1, filtered_age2.reindex(filtered_age2.index)])
        filtered_age.sort_values(["rating"], inplace=True, ascending=False)
        filtered_age.drop_duplicates(subset="movie_id",
                                     keep=False, inplace=True)
        result = filtered_age.head(10)
    movie_list = []
    for i in result['movie_id']:
        movie_list.append(idx_to_movie[str(i)])
    return movie_list
