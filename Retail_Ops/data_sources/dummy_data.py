import pandas as pd
import numpy as np

# Setting a random seed for reproducibility
np.random.seed(42)

num_stores = 20
days = pd.date_range(start="2022-01-01", end="2023-12-31")
n_days = len(days)

# Store IDs
store_ids = np.arange(1, num_stores + 1)

# Generate data
data = []

for store_id in store_ids:
    # Introduce a yearly seasonality component and a slight trend
    trend = np.linspace(0, 500, n_days)  # Small upward trend
    seasonality = 2000 * np.sin(2 * np.pi * np.arange(n_days) / 365)  # Yearly seasonality
    noise = np.random.normal(0, 800, n_days)  # Random noise
    
    # Generate sales data with seasonality, trend, and noise
    sales = np.round(3000 + trend + seasonality + noise, 2)
    sales = np.clip(sales, 1000, 9999)  # Ensure sales remain within a realistic range

    # Generate foot traffic, more tightly correlated with sales
    foot_traffic = np.round(sales * 0.1 + np.random.normal(0, 20, n_days)).astype(int)

    # Generate staff count, more closely tied to foot traffic
    staff_count = np.maximum((foot_traffic // 30).astype(int) + np.random.randint(0, 3, n_days), 3)

    # Set hours worked per staff member to be more dynamic
    hours_worked_per_staff = np.random.uniform(6, 8, n_days)

    # Calculate total labor hours by multiplying staff count by hours worked per staff
    labor_hours = staff_count * hours_worked_per_staff

    # Generate inventory levels with a stronger negative correlation to sales and a lag effect
    inventory_level = np.round(1500 - (sales * 0.08) + np.random.normal(0, 50, n_days)).astype(int)
    inventory_level = np.clip(inventory_level, 200, 1500)  # Ensure inventory levels remain realistic

    # Introduce promotions more strategically (e.g., more promotions during low sales periods)
    promotions = (sales < np.percentile(sales, 30)).astype(int)  # Promote during low sales

    # Compile the store data
    store_data = pd.DataFrame({
        "Date": days,
        "Store_ID": store_id,
        "Sales": sales,
        "Foot_Traffic": foot_traffic,
        "Staff_Count": staff_count,
        "Avg_Hourly_Rate": np.round(np.random.normal(15, 1.5, n_days), 2),
        "Hours_Worked": np.round(hours_worked_per_staff, 2),
        "Labor_Hours": np.round(labor_hours, 2),
        "Inventory_Level": inventory_level,
        "Promotions": promotions,
    })

    data.append(store_data)

# Combine data for all stores
df = pd.concat(data).reset_index(drop=True)

# Save the dataset to a CSV file
df.to_csv("Retail_Ops/data_sources/retail_store_data.csv", index=False)
