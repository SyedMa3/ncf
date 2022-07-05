import pandas as pd
import numpy as np

data = pd.read_csv('./data/ratings.csv')
data['sort_latest'] = data.groupby(['userId'])['timestamp'].rank(method='first', ascending=False)

train = data[data['sort_latest'] != 1]
test = data[data['sort_latest'] == 1]


num_users = len(data['userId'].unique())
num_movies = len(data['movieId'].unique())

train.loc[:, 'rating'] = 1
test.loc[:, 'rating'] = 1

all_movieIds = data['movieId'].unique()

users, items, labels = [], [], []

user_item_set = set(zip(train['userId'], train['movieId']))

num_negatives = 4

for (u,i) in user_item_set:
    users.append(u)
    items.append(i)
    labels.append(1)

    for _ in range(num_negatives):
        negative_item = np.random.choice(all_movieIds)

        while(u, negative_item) in user_item_set:
            negative_item = np.random.choice(all_movieIds)

        users.append(u)
        items.append(negative_item)
        labels.append(0)