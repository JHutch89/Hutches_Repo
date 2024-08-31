import streamlit as st
import pandas as pd
import numpy as np
from pmdarima import auto_arima
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Set the page configuration
st.set_page_config(page_title="Store Sales Forecasting", layout="wide")

# Load the data
retail_data = pd.read_csv("Retail_Ops/data_sources/retail_store_data.csv")

# Convert the Date column to datetime format
retail_data['Date'] = pd.to_datetime(retail_data['Date'])

# Title of the app
st.title("Store Sales Forecasting")

# Sidebar for user inputs
st.sidebar.header("Select Store")
store_id = st.sidebar.selectbox("Choose the Store ID:", retail_data['Store_ID'].unique())

# Filter data for the selected store
store_data = retail_data[retail_data['Store_ID'] == store_id].set_index('Date')

# Aggregate the data to weekly sales
weekly_sales_data = store_data['Sales'].resample('W').sum()

# Split the data into training and test sets (80% train, 20% test)
train_size = int(len(weekly_sales_data) * 0.8)
train, test = weekly_sales_data[:train_size], weekly_sales_data[train_size:]

# Automatically find the best p, d, q parameters using auto_arima
auto_model = auto_arima(train, 
                        start_p=0, start_q=0,
                        max_p=5, max_q=5,
                        d=None,  # Let the function decide the optimal 'd'
                        seasonal=False,  # Assuming no seasonality; set to True for SARIMA
                        trace=False,  # Don't print the results to the console
                        error_action='ignore',  # Ignore errors and keep going
                        suppress_warnings=True,
                        stepwise=True,  # Use stepwise search to reduce computation time
                        n_jobs=-1)  # Use all cores to speed up the process

# Forecast the test period
forecast = auto_model.predict(n_periods=len(test))

# Calculate accuracy metrics
mae = mean_absolute_error(test, forecast)
mse = mean_squared_error(test, forecast)
rmse = np.sqrt(mse)

# Display the SARIMAX model summary
st.subheader(f"SARIMAX Model Summary for Store {store_id}")
st.text(auto_model.summary())

# Display the accuracy metrics
st.subheader("Model Accuracy Metrics")
st.write(f"**Mean Absolute Error (MAE):** {mae:.2f}")
st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")
st.write(f"**Root Mean Squared Error (RMSE):** {rmse:.2f}")

# Create a DataFrame to show actual vs. predicted sales
results_df = pd.DataFrame({
    "Date": test.index,
    "Actual Sales": test.values,
    "Predicted Sales": forecast
})

# Display the actual vs. predicted sales in a table
st.subheader("Weekly Actual vs. Predicted Sales")
st.dataframe(results_df)

# Plot the historical sales, the forecast, and the test data
st.subheader(f"Weekly Sales Forecasting for Store {store_id}")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(train, label="Training Data")
ax.plot(test, label="Test Data", color='orange')
ax.plot(test.index, forecast, label="Forecasted Sales", linestyle='--', color='green')
ax.legend()
ax.set_title(f"Weekly Sales Forecasting for Store {store_id} using Auto ARIMA")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
st.pyplot(fig)
