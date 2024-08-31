import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import streamlit as st

# Load the data
df = pd.read_csv("Retail_Ops/data_sources/retail_store_data.csv")

# Define features (input variables) and the target (output variable)
features = ['Staff_Count', 'Inventory_Level', 'Promotions']  # You can add more features as needed
target = 'Sales'  # Target is the actual sales

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.3, random_state=42)

# Train a Random Forest Regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict sales on the test set
y_pred = model.predict(X_test)

# Calculate the performance of the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Use the model to predict optimal sales for the entire dataset
df['Optimal_Sales'] = model.predict(df[features])

# Calculate missed sales as the difference between optimal sales and actual sales
df['Missed_Sales'] = df['Optimal_Sales'] - df['Sales']
df['Missed_Sales'] = df['Missed_Sales'].clip(lower=0)  # Ensure missed sales are non-negative

# Summarize missed sales by store
missed_sales_summary = df.groupby('Store_ID')['Missed_Sales'].sum().reset_index()

# Streamlit app configuration
st.set_page_config(page_title="Regression-Based Missed Sales Analysis", layout="wide")

st.title("Regression-Based Missed Sales Analysis")

# Display model performance
st.write(f"Model Mean Squared Error: {mse:.2f}")

# Show the coefficients or feature importance if using a linear model or tree-based model
if hasattr(model, 'feature_importances_'):
    st.subheader("Feature Importances")
    feature_importances = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    })
    st.dataframe(feature_importances)

# Display missed sales summary for all stores
st.subheader("Summary of Missed Sales by Store")
st.dataframe(missed_sales_summary)

# Allow user to input specific store ID for detailed analysis
store_id = st.sidebar.selectbox("Choose the Store ID:", df['Store_ID'].unique())

# Display detailed data for the selected store
store_data = df[df['Store_ID'] == store_id]

st.subheader(f"Detailed Missed Sales Data for Store {store_id}")
st.dataframe(store_data[['Date', 'Sales', 'Optimal_Sales', 'Missed_Sales']])

# Optional: Save the detailed analysis for the selected store to a CSV file
if st.button("Save Detailed Analysis to CSV"):
    store_data.to_csv(f"Retail_Ops/data_sources/store_{store_id}_missed_sales_analysis.csv", index=False)
    st.success(f"Data saved to store_{store_id}_missed_sales_analysis.csv")
