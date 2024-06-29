import pandas as pd
import streamlit as st
from datetime import datetime

calendar = [
    ["4/20/24", "Pinelands", "9:33am", "$89"],
    ["5/18/24", "Middletown CC", "9:40am", "$77"],
    ["6/29/24", "Twisted Dune", "9:30am", "$110"],
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


member_snpsht = [
    ["Jason Hutches", "$80", "26.8"],
    ["Dave Cunningham", "$55","23.1"],
    ["Alex Taraschi", "$30","20.8"],
    ["Ken Cooper", "$25","31.4"],
    ["Chick Campbell", "$15","34.8"],
    ["Tom Taraschi", "$35","27.7"],
    ["Rich Hamner", "$15","26.4"],
    ["Shawn Frick", "$20","28.4"],
    ["Mark McDermott", "$0","28.7"],
    ["Kyle McClintock", "$0","21.9"],
    ["Keith Kalbach", "$20","33.7"],
    ["Don Latka", "$20","28.2"]
]

snpst = pd.DataFrame(member_snpsht, columns=["Golfer", "Winnings", "HC"])
snpst = snpst.sort_values(by='Golfer')
snpst.set_index("Golfer", inplace=True)


# Streamlit App setup
st.title("SJMGA 2024 Schedule | League Dues")
image_path = "golf/pages/golf_cal.jpg"
st.image(image_path, width=300)

st.write("SJMGA 2024 Schedule")
st.dataframe(sjmga_2024,500, None)
st.write("")
st.write("")
st.write("SJMGA 2024 Snapshot")
st.dataframe(snpst,1000, 450)
st.write("")
st.write("")
st.title("Putting at Twisted Dune")
image_path2 = "golf/pages/fast_greens.jpg"
st.image(image_path2, width=300)

