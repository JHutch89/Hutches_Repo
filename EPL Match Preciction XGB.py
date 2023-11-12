import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Read CSV file with explicit encoding
epl = pd.read_csv('/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/CSVs/EPL_Data.csv')

# Drop irrelevant features
features = epl.drop(['Date', 'Winner', 'Referee'], axis=1)

# Convert categorical variables to numerical using one-hot encoding
features_encoded = pd.get_dummies(features, columns=['HomeTeam', 'AwayTeam'])

# Extract target variable
target = epl['Winner']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_encoded, target, test_size=0.2, random_state=42)

# Initialize and train the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Create a Streamlit app
st.title("Football Result Prediction App")

# User input for home and away teams
home_team_options = features['HomeTeam'].unique()
away_team_options = features['AwayTeam'].unique()

home_team_selected = st.selectbox("Select Home Team:", home_team_options)
away_team_selected = st.selectbox("Select Away Team:", away_team_options)

# Manually create a DataFrame for user input with the correct structure
user_input = pd.DataFrame({
    'HomeTeam': [home_team_selected],
    'AwayTeam': [away_team_selected],
    'Home Goals': [0],
    'Away Goals': [0],
    'HomeShots': [0],
    'AwayShots': [0],
    'HomeShotsOnTarget': [0],
    'AwayShotsOnTarget': [0],
    'HomeFouls': [0],
    'AwayFouls': [0],
    'HomeCorners': [0],
    'AwayCorners': [0],
    'HomeYellows': [0],
    'AwayYellows': [0],
    'HomeReds': [0],
    'AwayReds': [0],
})

# Utility function for one-hot encoding
def one_hot_encode_input(input_df, training_columns):
    encoded_df = pd.get_dummies(input_df, columns=['HomeTeam', 'AwayTeam'])
    # Reorder columns to match the order during training
    encoded_df = encoded_df.reindex(columns=training_columns, fill_value=0)
    return encoded_df

# Apply one-hot encoding to user input with utility function
user_input_encoded = one_hot_encode_input(user_input, X_train.columns)

# Make predictions on user input
user_prediction = rf_classifier.predict(user_input_encoded)

# Display the result
st.subheader("Result Prediction:")
st.write(f"The predicted winner is: {user_prediction[0]}")
