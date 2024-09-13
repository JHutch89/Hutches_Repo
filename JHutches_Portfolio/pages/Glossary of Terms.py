import streamlit as st
import pandas as pd

# Load the updated glossary CSV file
df = pd.read_csv("Retail_Ops/data_sources/sarimax_glossary.csv")

# Display the table in Streamlit
st.header("Glossary/Interpretations)")
st.dataframe(df)
