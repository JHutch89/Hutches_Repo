import pandas as pd
import streamlit as st
from datetime import datetime

calendar = [
    ["4/20/24", "Pinelands", "9:33am", "$89"],
    ["5/18/24", "Middletown CC", "9:40am", "$77"],
    ["6/29/24", "Twisted Dune", "9:30am", "$110"],
    ["7/20/24", "Town and Country", "9:30am", "$95"],
    ["8/25/24", "Cream Ridge", "9:36am", "$70"],
    ["9/14/24", "Buena Vista", "9:34", "$70"],
    ["10/12/24", "Mercer Oaks", "TBD", "TBD"],
    ["11/2/24", "Scotland Run *", "TBD", "TBD"]
]

sjmga_2024 = pd.DataFrame(calendar, columns=["Date", "Course", "Time", "Price"])
sjmga_2024['Date'] = pd.to_datetime(sjmga_2024['Date'], format='%m/%d/%y')
sjmga_2024['Date'] = sjmga_2024['Date'].dt.date
sjmga_2024.set_index("Date", inplace=True)


member_snpsht = [
    ["Jason Hutches", "$95", "23.9"],
    ["Dave Cunningham", "$60","23"],
    ["Alex Taraschi", "$50","20"],
    ["Ken Cooper", "$45","31.4"],
    ["Chick Campbell", "$40","35.1"],
    ["Tom Taraschi", "$50","28.6"],
    ["Rich Hamner", "$30","26.4"],
    ["Shawn Frick", "$30","28.3"],
    ["Mark McDermott", "$30","27.5"],
    ["Kyle McClintock", "$10","26.9"],
    ["Keith Kalbach", "$45","35.3"],
    ["Don Latka", "$40","28.3"]
]

snpst = pd.DataFrame(member_snpsht, columns=["Golfer", "Winnings", "HC"])
snpst = snpst.sort_values(by='Golfer')
snpst.set_index("Golfer", inplace=True)


# Streamlit App setup
st.title("SJMGA 2024 Schedule | League Dues")
image_path = "Golf/pages/golf_cal.jpg"
st.image(image_path, width=300)

st.write("SJMGA 2024 Schedule")
st.dataframe(sjmga_2024,500, None)
st.write("")
st.write("")
st.write("SJMGA 2024 Snapshot")
st.dataframe(snpst,1000, 450)
# st.write("")
# st.write("")
# st.title("Putting at Twisted Dune")
# image_path2 = "Golf/pages/fast_greens.jpg"
# st.image(image_path2, width=300)

