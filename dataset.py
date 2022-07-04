import pandas as pd
import numpy as np

train = pd.read_csv('./drive/MyDrive/ncf/data/train.csv')
test = pd.read_csv('./drive/MyDrive/ncf/data/test.csv')

num_users = len(dataset['userId'].unique())
num_movies = len(dataset['movieId'].unique())