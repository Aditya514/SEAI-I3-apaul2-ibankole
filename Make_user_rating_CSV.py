import pandas as pd
import pickle


create_csv = False
with open('user_row_dict.pkl', 'rb') as f:
    loaded_user_df_dict = pickle.load(f)
    #print(loaded_user_df_dict)
    print("")

with open('movie_col_dict.pkl', 'rb') as f:
    loaded_movie_df_dict = pickle.load(f)
    #print(loaded_movie_df_dict.keys())
    print("")
       
loaded_user_movie_ratings_df = pd.read_pickle("movie_ratings_df.pkl")


#Label columns and rows
#labled columns
#loaded_user_movie_ratings_df.columns = list(loaded_movie_df_dict.keys())

#label rows
loaded_user_movie_ratings_df = loaded_user_movie_ratings_df.assign(users=list(loaded_user_df_dict.keys()))

loaded_user_movie_ratings_df.set_index('users',inplace=True)
loaded_user_movie_ratings_df.columns.name = 'movies'
#loaded_user_movie_ratings_df.reset_index(inplace=True)
#print(loaded_user_movie_ratings_df.head())
#print(loaded_user_movie_ratings_df.index.name)
loaded_user_movie_ratings_df_long = loaded_user_movie_ratings_df.reset_index().melt(id_vars='users',var_name='movies')
print(loaded_user_movie_ratings_df_long.head())

if create_csv:
	loaded_user_movie_ratings_df_long.to_csv("H2O_MovieData.csv")
