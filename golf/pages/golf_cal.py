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
    ["Jason Hutches", "$60", "27.6"],
    ["Dave Cunningham", "$35","23.6"],
    ["Alex Taraschi", "$25","21.6"],
    ["Ken Cooper", "$15","30.7"],
    ["Chick Campbell", "$15","34.8"],
    ["Tom Taraschi", "$10","28"],
    ["Rich Hamner", "$15","25.8"],
    ["Shawn Frick", "$20","28.2"],
    ["Mark McDermott", "$0","28.7"],
    ["Kyle McClintock", "$0","21"],
    ["Keith Kalbach", "$10","33.7"],
    ["Don Latka", "$0","29"]
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
st.title("Jason and Dave have unlocked the Pin Seeker Achievement")
image_path2 = "golf/pages/pinseeker.jpg"
st.image(image_path2, width=300)

