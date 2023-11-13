import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score  # Import accuracy_score

# Read CSV file with explicit encoding
epl = pd.read_csv('CSVs/EPL_Data.csv')

# Select features for training
features = epl[['HomeTeam', 'AwayTeam', 'Referee']]

# Convert categorical variables to numerical using one-hot encoding
features_encoded = pd.get_dummies(features, columns=['HomeTeam', 'AwayTeam', 'Referee'])

# Extract target variable
target = epl['Winner']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_encoded, target, test_size=0.2, random_state=42)

# Initialize and train the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Create a Streamlit app
st.title("EPL Prediction App")

# User input for home and away teams
home_team_options = features['HomeTeam'].unique()
away_team_options = features['AwayTeam'].unique()
referee_options = features['Referee'].unique()

home_team_selected = st.selectbox("Select Home Team:", home_team_options)
away_team_selected = st.selectbox("Select Away Team:", away_team_options)
referee_selected = st.selectbox("Select Referee:", referee_options)

# Manually create a DataFrame for user input with the correct structure
user_input = pd.DataFrame({
    'HomeTeam': [home_team_selected],
    'AwayTeam': [away_team_selected],
    'Referee': [referee_selected],
})

# Utility function for one-hot encoding
def one_hot_encode_input(input_df, training_columns):
    encoded_df = pd.get_dummies(input_df, columns=['HomeTeam', 'AwayTeam', 'Referee'])
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

# Calculate and display model accuracy
y_pred = rf_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Model Accuracy: {accuracy:.2%}")
