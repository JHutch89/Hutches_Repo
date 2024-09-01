import streamlit as st
import joblib
import numpy as np

# Load the encoders, scaler, and model
le_home_team = joblib.load('Euro24_Data/le_home_team.pkl')
le_away_team = joblib.load('Euro24_Data/le_away_team.pkl')
le_stadium = joblib.load('Euro24_Data/le_stadium.pkl')
le_referee = joblib.load('Euro24_Data/le_referee.pkl')
scaler = joblib.load('Euro24_Data/scaler.pkl')
model = joblib.load('Euro24_Data/score_prediction_model.pkl')

# Mapping from country names to flag emojis
country_flags = {
    'Albania': '🇦🇱',
    'Austria': '🇦🇹',
    'Belgium': '🇧🇪',
    'Croatia': '🇭🇷',
    'Czech Republic': '🇨🇿',
    'Denmark': '🇩🇰',
    'England': '🇬🇧',  # Using UK flag for England
    'France': '🇫🇷',
    'Georgia': '🇬🇪',
    'Germany': '🇩🇪',
    'Hungary': '🇭🇺',
    'Italy': '🇮🇹',
    'Netherlands': '🇳🇱',
    'Poland': '🇵🇱',
    'Portugal': '🇵🇹',
    'Romania': '🇷🇴',
    'Scotland': '🇬🇧',  # Using UK flag for Scotland
    'Serbia': '🇷🇸',
    'Slovakia': '🇸🇰',
    'Slovenia': '🇸🇮',
    'Spain': '🇪🇸',
    'Switzerland': '🇨🇭',
    'Turkey': '🇹🇷',
    'Ukraine': '🇺🇦'
}

st.title('Euro Cup 2024 Score Prediction')
image_path = "Euro24_Data/euro_ball.jpeg"
st.image(image_path, width=350)

home_team = st.selectbox('Select Home Team', le_home_team.classes_)
away_team = st.selectbox('Select Away Team', le_away_team.classes_)
stadium = st.selectbox('Select Stadium', le_stadium.classes_)
referee = st.selectbox('Select Referee', le_referee.classes_)

if st.button('Predict Score'):
    # Encode inputs
    home_team_encoded = le_home_team.transform([home_team])[0]
    away_team_encoded = le_away_team.transform([away_team])[0]
    stadium_encoded = le_stadium.transform([stadium])[0]
    referee_encoded = le_referee.transform([referee])[0]

    # Create input array
    input_array = np.array([[home_team_encoded, away_team_encoded, stadium_encoded, referee_encoded]])
    input_array = scaler.transform(input_array)

    # Predict score
    predicted_score = model.predict(input_array)

    # Get team names back from encoded values
    home_team_name = le_home_team.inverse_transform([home_team_encoded])[0]
    away_team_name = le_away_team.inverse_transform([away_team_encoded])[0]

    # Display the prediction with flags and names
    home_team_flag = country_flags[home_team_name]
    away_team_flag = country_flags[away_team_name]

    st.write(f'Predicted Score: {home_team_name} {home_team_flag} {int(predicted_score[0][0])} - {int(predicted_score[0][1])} {away_team_flag} {away_team_name}')

st.write("")
st.write("")
st.write("")
st.write("")
st.header("Project Overview")
st.write("""
I'm a huge soccer fan, and I wanted to combine my love for soccer with my love for data.  I've done plenty of work in regression, clustering and other prediction models...
but I haven't done much using neural networks.  So, I wanted to have a go at building a predictive model using MLPRegressor, which is a class of neural networks used in regression.
I am still working through some feature engineering, but I do hope you enjoy playing around with some different scenarios!
         
## What is this model?
This model is a neural network regressor built using the Multi-Layer Perceptron (MLP) algorithm. It has been trained on historical Euro Cup match data, including details about the teams, stadium, and referees, to predict the outcomes of future matches.

## How does it work?
1. **Data Collection**: Historical match data is fetched using data provided by StatsBomb
2. **Data Preprocessing**: Categorical features (team names, stadiums, referees) are encoded into numerical values. The data is then split into training and testing sets and normalized.
3. **Model Training**: The MLPRegressor model is trained on the training data using features to predict the scores.
4. **Prediction**: The model takes the input of selected teams, stadium, and referee, and predicts the likely scores for the home and away teams.

## What does this accomplish?
- Predicts the scores of random Euro Cup matches based on historical data.
- Explores the impact of different factors (teams, stadiums, and referees) on the match outcomes.

## How to use the app:
1. Select the home team and away team from the dropdown menus.
2. Choose the stadium and referee for the match.
3. Click the 'Predict Score' button to see the predicted scores!
""")
