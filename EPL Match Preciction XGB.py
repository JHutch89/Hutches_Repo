import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import df_options

df_options.options()

epl = pd.read_csv('/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/CSVs/premier_league_all_matches.csv')
columns_to_drop = ['Week', 'Date', 'Time', 'Attendance', 'Venue', 'Referee']
epl = epl.drop(columns = columns_to_drop)

# Convert match scores to goal difference
epl['Goal_Difference'] = epl['Score'].apply(lambda x: eval(x.replace('–', '-')))
epl['Outcome'] = epl['Goal_Difference'].apply(lambda x: 'Win' if x > 0 else ('Draw' if x == 0 else 'Loss'))

# Convert categorical features to numerical using Label Encoding
label_encoder = LabelEncoder()
epl['Home_Team'] = label_encoder.fit_transform(epl['Home_Team'])
epl['Away_Team'] = label_encoder.transform(epl['Away_Team'])
epl['Outcome'] = label_encoder.fit_transform(epl['Outcome'])  # Use fit_transform on the entire 'Outcome' column

# Extract target variable (outcome) and features
X = epl.drop(['Score', 'Outcome', 'Goal_Difference'], axis=1)
y = epl['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the XGBoost classifier
model = XGBClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')