import streamlit as st
import pandas as pd
import pickle
import surprise

st.title("Stuff Recommender")

st.write("## This is a real app for stuff!")

user = st.number_input("What is your UserID?", min_value=1, max_value=610)

genre = st.multiselect("Movie Genre",
    options=['action', 'adventure','animation', 'children', 'comedy','crime','documentary','drama','fantasy','film-noir','horror','musical','mystery','romance','sci-fi','thriller','war','western'])


num_recs = st.number_input("How many recommendations would you like?", min_value=1, max_value=10)

f=open('./data/final_fitted_model.sav', 'rb')
final_model=pickle.load(f)
f.close()

users_movies_seen = pd.read_csv('./data/users_movies_seen.csv',index_col='userId')
movies = pd.read_csv('./data/movies_cleaned.csv', index_col=0)

def recommender2(user,genre,num_recs):
    #using the train data
    #create the seen_movie
    seen_movie = list(users_movies_seen.loc[user, 'movieId'])

    #create df with all the unseen/unrated movies
    train_copy = movies.copy()
    train_copy2 = train_copy.set_index('movieId')

    #using the not_seen df, create a rating for a user
    not_seen = train_copy2.drop(index = seen_movie)

    #subsetting the df to unseen movies of a certain genre
    seen_test = pd.DataFrame(columns=['genres', 'Title', 'year_released'])
    for x in genre:
        for row, data in not_seen.iterrows():
            if x in not_seen['genres'][row]:
                seen_test.loc[row] = list(not_seen.loc[row,:])
    
    #reset not_seen index
    seen_test = seen_test.reset_index()
    
    #creating an est rating and the sorted it
    seen_test['est_rating'] = seen_test['index'].apply(lambda x: final_model.predict(user, x).est)
    seen_test.sort_values(by='est_rating', ascending=False, inplace=True)

    #returns the recommendations that the model predicts to be the highest rating
    return (seen_test[['Title', 'genres']].head(num_recs))

hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)

run = st.button("click to run")


if run:
    results = recommender2(user,genre,num_recs)
    st.table(results['Title'])