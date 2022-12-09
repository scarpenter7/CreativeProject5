import numpy as np 
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn import preprocessing



def train_model():
    df = pd.read_csv('song_data.csv')
    target_col = df['danceability'].values
    train_data = df.loc[:, df.columns != 'danceability']
    train_data = train_data.loc[:, train_data.columns != 'song_name']
    train_data = train_data.loc[:, train_data.columns != 'key']
    train_data = train_data.loc[:, train_data.columns != 'audio_mode']
    train_data = train_data.loc[:, train_data.columns != 'time_signature']
    
    min_max_scaler = preprocessing.MinMaxScaler()
    scaled_train_data = min_max_scaler.fit_transform(train_data)

    model = Ridge().fit(scaled_train_data, target_col)
    
    return model
    
    