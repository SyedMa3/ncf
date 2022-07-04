import pandas as pd
import numpy as np

train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')
dataset = pd.read_csv('./data/ratings.csv')

num_users = len(dataset['userId'].unique())
num_movies = len(dataset['movieId'].unique())