import pandas as pd
import streamlit as st
from datetime import datetime

calendar = [
    ["4/20/24", "Pinelands", "9:33am", "$89"],
    ["5/18/24", "Makefield Highlands", "TBD", "TBD"],
    ["6/29/24", "Harbor Pines", "TBD", "TBD"],
    ["7/20/24", "Town and Country", "TBD", "TBD"],
    ["8/10/24", "Cream Ridge", "TBD", "TBD"],
    ["9/14/24", "Golden Pheasant", "TBD", "TBD"],
    ["10/12/24", "Mercer Oaks", "TBD", "TBD"],
    ["11/2/24", "Scotland Run *", "TBD", "TBD"]
]

sjmga_2024 = pd.DataFrame(calendar, columns=["Date", "Course", "Time", "Price"])
sjmga_2024['Date'] = pd.to_datetime(sjmga_2024['Date'], format='%m/%d/%y')
sjmga_2024['Date'] = sjmga_2024['Date'].dt.date
sjmga_2024.set_index("Date", inplace=True)


dues = [
    ["Jason", "$145"],
    ["Dave", "$145"],
    ["Alex", "$145"],
    ["Ken", "$145"],
    ["Chick", "$85"],
    ["Tom", "$145"],
    ["Rich", "$65"],
    ["Shawn", "$115"],
    ["Mark", "$145"],
    ["Kyle", "$145"],
    ["Keith", "$145"],
    ["Don", "$145"]
]

dues_2024 = pd.DataFrame(dues, columns=["Golfer", "Outstanding Dues"])
dues_2024 = dues_2024.sort_values(by='Golfer')
dues_2024.set_index("Golfer", inplace=True)

# Streamlit App setup
st.title("SJMGA 2024 Schedule | League Dues")
image_path = "golf/pages/golf_cal.jpg"
st.image(image_path, width=300)

st.write("SJMGA 2024 Schedule")
st.dataframe(sjmga_2024,500, None)
st.write("")
st.write("")
st.write("Outstanding Dues")
st.dataframe(dues_2024,250, 450)
