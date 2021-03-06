# Neural Collaborative Filtering

This is an implementation of Neural Collaborative Filtering for a movie recommendation system based on the [MovieLens 1M Dataset](https://grouplens.org/datasets/movielens/).

### References:

[Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031)

I wanted to build a movie recommendation system and use deep learning for it. So I came across NCF and it seemed like a good starting point so I implemented it.

To tackle the cold-start problem, we can ask the users to mention a few movies he liked and then proceed.

## Evaluation Protocols:

To evaluate the performance of item recommendation, we use the *leave-one-out* evaluation.

Since it is too time consuming to rate every non-interacted movie, we take random 100 movies and display the top 10 movies for that user.

## Structure of Application:

- [dataset.py](dataset.py) - Split the dataset into train and test and turned data into implicit feedback.
- [neuMF.ipynb](model/neuMF.ipynb) - Train the model and predict 10 movies for a given user.
- [model.h5](model.h5) - Saved model so that I can fine-tune on new users.