import psycopg2 
import pandas as pd
from xgboost import XGBRegressor
from sqlalchemy import create_engine 

## Credentials to DB
db_config = {
    "dbname": "your_database_name",
    "user": "your_username",
    "password": "your_password",
    "host": "your_database_host",
    "port": "5432"
}

# Establish connection to the AWS database
conn = psycopg2.connect(**db_config)

# Query to fetch data
query = """
SELECT 
    t1.id AS common_id,
    t1.dimension1,
    t2.dimension2,
    t3.measure1,
    t4.measure2,
    t5.dimension3
FROM table1 t1
LEFT JOIN table2 t2 
    ON t1.id = t2.id
JOIN table3 t3 
    ON t1.id = t3.id
LEFT JOIN table4 t4 
    ON t1.id = t4.id AND t4.date IS NOT NULL
JOIN table5 t5 
    ON t1.id = t5.id;
"""

df = pd.read_sql(query, conn)

## Close the connection
conn.close()

## Prep data for model
X = df[['dimension1', 'dimension2', 'dimension3']].values
y = df['measure1'].values

## Training super simple XGBoost model
model = XGBRegressor(n_estimators=10, max_depth=3, random_state=42)
model.fit(X, y)

## Push predictions to the DataFrame
df['predicted_measure'] = model.predict(X)

# Push results to DB
engine = create_engine(f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}")
df.to_sql('predicted_results', engine, if_exists='replace', index=False)