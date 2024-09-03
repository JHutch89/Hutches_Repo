import streamlit as st
import pandas as pd
import numpy as np
from pmdarima import auto_arima
import matplotlib.pyplot as plt

# Set the page configuration
st.set_page_config(page_title="Store Sales Forecasting with Auto SARIMA", layout="wide")

# Load the data
retail_data = pd.read_csv("Retail_Ops/data_sources/retail_store_data.csv")

# Convert the Date column to datetime format
retail_data['Date'] = pd.to_datetime(retail_data['Date'])

# Title of the app
st.title("Store Sales Forecasting with Auto SARIMA")

# Sidebar for user inputs
st.sidebar.header("Select Store")
store_id = st.sidebar.selectbox("Choose the Store ID:", retail_data['Store_ID'].unique())

# Filter data for the selected store
store_data = retail_data[retail_data['Store_ID'] == store_id].set_index('Date')

# Aggregate the data to weekly sales
weekly_sales_data = store_data['Sales'].resample('W').sum()

# Automatically find the best seasonal p, d, q, P, D, Q parameters using auto_arima
auto_model = auto_arima(weekly_sales_data, 
                        start_p=0, start_q=0,
                        max_p=5, max_q=5,
                        d=None,  # Let the function decide the optimal 'd'
                        seasonal=True,  # Enable seasonal modeling
                        m=52,  # Seasonal cycle length (52 weeks for yearly seasonality)
                        start_P=0, start_Q=0,
                        max_P=5, max_Q=5,
                        D=None,  # Let the function decide the optimal seasonal differencing
                        trace=True,  # Print the results to the console
                        error_action='ignore',  # Ignore errors and keep going
                        suppress_warnings=True,
                        stepwise=True,  # Use stepwise search to reduce computation time
                        n_jobs=-1)  # Use all cores to speed up the process

# Print the best model's summary
st.subheader(f"SARIMA Model Summary for Store {store_id}")

# Capture the model summary as a string
summary_str = auto_model.summary().as_text()

# Format numbers to avoid scientific notation
formatted_summary = []
for line in summary_str.splitlines():
    parts = line.split()
    if len(parts) == 0:  # Skip empty lines
        formatted_summary.append(line)
    elif any(keyword in line for keyword in ["coef", "std err", "z", "P>|z|", "0.025", "0.975"]):  # Keep header lines intact
        formatted_summary.append(line)
    else:
        try:
            # Check if the line contains numeric data and format it
            formatted_line = f"{parts[0]:<20} {float(parts[1]):,.2f} {float(parts[2]):,.2f} {float(parts[3]):,.2f} {float(parts[4]):,.2f} {float(parts[5]):,.2f} {float(parts[6]):,.2f}"
            formatted_summary.append(formatted_line)
        except (ValueError, IndexError):
            # If conversion fails, append the line as is
            formatted_summary.append(line)

st.text("\n".join(formatted_summary))

# Forecast the next 52 weeks (1 year)
forecast_periods = 12
forecast = np.round(auto_model.predict(n_periods=forecast_periods), 2)  # Round the forecasted values

# Create future dates for the forecast
future_dates = pd.date_range(start=weekly_sales_data.index[-1] + pd.Timedelta(weeks=1), 
                             periods=forecast_periods, freq='W')

# Create a DataFrame to hold the forecast
forecast_df = pd.DataFrame({
    "Date": future_dates,
    "Predicted Sales": forecast
})

# Display the forecasted sales in a table
st.subheader(f"Forecasted Sales for the Next {forecast_periods} Weeks")
st.dataframe(forecast_df)

# Plot the historical sales and the forecast
st.subheader(f"Weekly Sales Forecasting with Seasonality for Store {store_id}")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(weekly_sales_data, label="Historical Sales")
ax.plot(future_dates, forecast, label="Forecasted Sales", linestyle='--', color='green')
ax.legend()
ax.set_title(f"Weekly Sales Forecasting for Store {store_id} using Auto SARIMA")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
st.pyplot(fig,use_container_width=False)
