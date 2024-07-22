import streamlit as st
import joblib
import numpy as np

# Load the encoders, scaler, and model
le_home_team = joblib.load('Euro 24 Data/le_home_team.pkl')
le_away_team = joblib.load('Euro 24 Data/le_away_team.pkl')
le_stadium = joblib.load('Euro 24 Data/le_stadium.pkl')
le_referee = joblib.load('Euro 24 Data/le_referee.pkl')
scaler = joblib.load('Euro 24 Data/scaler.pkl')
model = joblib.load('Euro 24 Data/score_prediction_model.pkl')

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