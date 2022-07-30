import pandas as pd
import numpy as np

data = pd.read_csv('./data/ratings.csv')

# data_count = data.groupby(['userId']).count()
# data['count'] = data.groupby('userId').transform('count')
# data = data[data['count'] > 1]

# data['movie'] = data['movieId'].astype("category").cat.codes

# movie_lookup = data[['movie', 'movieId']].drop_duplicates()

data['sort_latest'] = data.groupby(['userId'])['timestamp'].rank(method='first', ascending=False)
train = data[data['sort_latest'] != 1]
test = data[data['sort_latest'] == 1]

num_users = max(data['userId'].unique())
num_movies = max(data['movieId'].unique())

train = train.assign(rating=1)
test = test.assign(rating=1)

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

dset = pd.DataFrame({'users': users,'items': items,'labels': labels})

print(test)