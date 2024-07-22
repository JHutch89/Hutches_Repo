import streamlit as st

# Show the code
st.header("Score Prediction Model Code")
code = '''
import pandas as pd
from statsbombpy import sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import joblib
import os
import emoji

## set pandas display options
def options():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('expand_frame_repr', False)

options()

## directory to save model and encoders
save_dir = 'Euro 24 Data'
## create the directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

## fetch match data from statsbombpy (THANK YOU STATSBOMB!!)
euro_data = sb.matches(competition_id=55, season_id=282)

## select relevant features
euro_data_features = euro_data[[
    'home_team', 
    'away_team',
    'home_score',
    'away_score',
    'stadium',
    'referee',
]]

## initialize label encoders for categorical features
le_home_team = LabelEncoder()
le_away_team = LabelEncoder()
le_stadium = LabelEncoder()
le_referee = LabelEncoder()

## fit and transform categorical features
euro_data_features.loc[:, 'home_team'] = le_home_team.fit_transform(euro_data_features['home_team'])
euro_data_features.loc[:, 'away_team'] = le_away_team.fit_transform(euro_data_features['away_team'])
euro_data_features.loc[:, 'stadium'] = le_stadium.fit_transform(euro_data_features['stadium'])
euro_data_features.loc[:, 'referee'] = le_referee.fit_transform(euro_data_features['referee'])

## define feature set and target variables
X = euro_data_features[['home_team', 'away_team', 'stadium', 'referee']]
y = euro_data_features[['home_score', 'away_score']]

## split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## initialize and fit the scaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

## convert target variables to numpy arrays
y_train = y_train.to_numpy()
y_test = y_test.to_numpy()

## initialize and train the neural network model
best_model = MLPRegressor(hidden_layer_sizes=(64, 32), activation='tanh', solver='sgd', learning_rate_init=0.001, max_iter=500)
best_model.fit(X_train, y_train)

## predict scores on the test set
y_pred = best_model.predict(X_test)

## calculate mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f'Best Test MSE: {mse}')

## check a few predictions
for i in range(10):
    print(f"Predicted: Home {y_pred[i][0]:.2f} - Away {y_pred[i][1]:.2f}, Actual: Home {y_test[i][0]} - Away {y_test[i][1]}")

## save the encoders and scaler for future use
joblib.dump(le_home_team, os.path.join(save_dir, 'le_home_team.pkl'))
joblib.dump(le_away_team, os.path.join(save_dir, 'le_away_team.pkl'))
joblib.dump(le_stadium, os.path.join(save_dir, 'le_stadium.pkl'))
joblib.dump(le_referee, os.path.join(save_dir, 'le_referee.pkl'))
joblib.dump(scaler, os.path.join(save_dir, 'scaler.pkl'))

## save the trained model
joblib.dump(best_model, os.path.join(save_dir, 'score_prediction_model.pkl'))


'''
st.code(code, language='python')
