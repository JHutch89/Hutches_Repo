import streamlit as st

# Show the code
st.header("Project Overview")
st.write("""
I'm a huge soccer fan, and I wanted to combine my love for soccer with my love for data.  I've done plenty of work in regression, clustering and other prediction models...
but I haven't done much using neural networks.  So, I wanted to have a go at building a predictive model, using MLPRegressor which is a class of neural networks used in regression.
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
