
import pandas as pd

dataset=pd.read_csv("H2O_MovieData.csv").sample(frac=1).reset_index(drop=True)[['users','movies','value']]
split=[int(len(dataset)*0.6),int(len(dataset)*0.8)]
train_dataset=dataset[:split[0]]
valid_dataset=dataset[split[0]:split[1]]
test_dataset=dataset[split[1]:]
train_dataset.to_csv("H2O_movie_train.csv",index=False)
valid_dataset.to_csv("H2O_movie_valid.csv",index=False)
test_dataset.to_csv("H2O_movie_test.csv",index=False)




