import pandas as pd
import pickle
import matplotlib.pyplot as plt

from surprise import Dataset, Reader, accuracy
from surprise.model_selection import cross_validate, train_test_split, GridSearchCV
from surprise.prediction_algorithms import SVD, SVDpp, NMF, BaselineOnly, NormalPredictor

plt.style.use('fast')
%matplotlib inline


#get the full training dataset
#so this is the full train data in surprise dataset
full_data = train_data.build_full_trainset()
#fit the full_data which is a surprise dataset
model.fit(full_data)

#creating a variable that only has the userid and movies that they've rated
#this uses the original train dataset not surprise's version
users_movies_seen = train[['movieId', 'userId']]
#setting user id as index to make it easier to use loc on it
users_movies_seen.set_index('userId')


#function to get stuff up
def stuff():
    user = input('userId: ')
    genre = input('What genres are you interested in? ')
    num_recs = input('How many recomendations would you like? ')

    #using the train data
    #create the seen_movie
    seen_movie = list(users_movies_seen.loc[user, 'movieId'])

    #create df with all the unseen/unrated movies
    train_copy = train.copy()
    not_seen = train_copy.drop(seen_movie)
    #using the not_seen df, create a rating for a user
    not_seen = not_seen[not_seen['genres'] == genre]
    not_seen['est_rating'] = not_seen['movieId'].apply(lambda x: best_model.predict(user, x).est)
    not_seen.sort_values(by='est_rating', ascending=False, inplace=True)

    return (not_seen.head(num_recs))


