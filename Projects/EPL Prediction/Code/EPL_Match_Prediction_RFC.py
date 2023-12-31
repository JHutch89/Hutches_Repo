import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Read CSV
epl = pd.read_csv('CSVs/EPL_Data.csv')

# Select features for training
features = epl[['HomeTeam', 'AwayTeam', 'Referee']]

# Convert categorical variables to numerical using one hot encoding
features_encoded = pd.get_dummies(features, columns=['HomeTeam', 'AwayTeam', 'Referee'])

# Extract target variable
target = epl['Winner']

# Split the data into training and testing 
X_train, X_test, y_train, y_test = train_test_split(features_encoded, target, test_size=0.2, random_state=42)

# Train the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Streamlit app Title
st.title("EPL Prediction App")

# Adding image to app
image_path = "images/EPL_Logo.png"
st.image(image_path, use_column_width=False, width=200)

# User input for home and away teams
home_team_options = sorted(features['HomeTeam'].unique())
away_team_options = sorted(features['AwayTeam'].unique())
referee_options = sorted(features['Referee'].unique())

home_team_selected = st.selectbox("Select Home Team:", home_team_options)
away_team_selected = st.selectbox("Select Away Team:", away_team_options)
referee_selected = st.selectbox("Select Referee:", referee_options)

# Create df based on user input
user_input = pd.DataFrame({
    'HomeTeam': [home_team_selected],
    'AwayTeam': [away_team_selected],
    'Referee': [referee_selected],
})

# One hot encoding function
def one_hot_encode_input(input_df, training_columns):
    encoded_df = pd.get_dummies(input_df, columns=['HomeTeam', 'AwayTeam', 'Referee'])
    # Reorder columns to match the order during training
    encoded_df = encoded_df.reindex(columns=training_columns, fill_value=0)
    return encoded_df

# Apply one hot encoding to user selection with one hot encoding function
user_input_encoded = one_hot_encode_input(user_input, X_train.columns)

# Predict outcome based on inputs
user_prediction = rf_classifier.predict(user_input_encoded)

# Display the results
st.subheader(f"The predicted winner is: {user_prediction[0]}")

# Calculate and display model accuracy
y_pred = rf_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Model Accuracy: {accuracy:.2%}")
