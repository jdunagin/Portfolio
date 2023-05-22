# Overview
The goal of this project was to create a subreddit recommender for users of Reddit, based on the usage of other users. I wanted to find patterns in the usage of different subreddits and use that information to predict what undiscovered subreddits a given user might like.

# Data
This data was acquired using Reddit's API. With that, I was able to pull a few hundred users, along with which subreddits they commented on and how many comments they had submitted on each.

# Methods
With that data, I created a recommender using a K-Nearest-Neighbors model. The model computed a user's neighbors based on similar comment histories, and then looked at what other subreddits they are commenting on that the user is not. The model was tuned for the optimal number of neighbors, along with the optimal distance metric. Others could use this notebook to download brand new data, and then retune the model and create a more up-to-date recommender.
