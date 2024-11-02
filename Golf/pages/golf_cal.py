import pandas as pd
import streamlit as st
from datetime import datetime

# Set up tournament calendar
calendar = [
    ["4/20/24", "Pinelands", "9:33am", "$89"],
    ["5/18/24", "Middletown CC", "9:40am", "$77"],
    ["6/29/24", "Twisted Dune", "9:30am", "$110"],
    ["7/20/24", "Town and Country", "9:30am", "$95"],
    ["8/25/24", "Cream Ridge", "9:36am", "$70"],
    ["9/14/24", "Buena Vista", "9:34am", "$70"],
    ["10/12/24", "Golden Pheasant", "12:00pm", "$86"],
    ["11/2/24", "Scotland Run", "10:00am", "$125"]
]

sjmga_2024 = pd.DataFrame(calendar, columns=["Date", "Course", "Time", "Price"])
sjmga_2024['Date'] = pd.to_datetime(sjmga_2024['Date'], format='%m/%d/%y')
sjmga_2024['Date'] = sjmga_2024['Date'].dt.date
sjmga_2024.set_index("Date", inplace=True)

# Set up golfer data
member_snpsht = [
    ["Jason Hutches", "$120", "22", 17.6],
    ["Dave Cunningham", "$95", "23", 18.4],
    ["Alex Taraschi", "$55", "21.9", 17.5],
    ["Ken Cooper", "$65", "31.6", 25.3],
    ["Chick Campbell", "$50", "36.3", 29.0],
    ["Tom Taraschi", "$80", "28.8", 23.0],
    ["Rich Hamner", "$70", "26.8", 21.4],
    ["Shawn Frick", "$30", "28.3", 22.7],
    ["Mark McDermott", "$50", "27.2", 21.8],
    ["Kyle McClintock", "$10", "26.9", 21.6],
    ["Keith Kalbach", "$45", "35.3", 28.2],
    ["Don Latka", "$75", "28.1", 22.5]
]

snpst = pd.DataFrame(member_snpsht, columns=["Golfer", "Winnings", "HC", "Championship HC"])
snpst = snpst.sort_values(by='Golfer')
snpst.set_index("Golfer", inplace=True)

# Streamlit App setup
st.title("SJMGA 2024 Schedule | League Dues")
image_path = "Golf/pages/golf_cal.jpg"
st.image(image_path, width=300)

# Display calendar and golfer data
st.write("SJMGA 2024 Schedule")
st.dataframe(sjmga_2024, 500, None)
st.write("")
st.write("")
st.write("SJMGA 2024 Snapshot")
st.dataframe(snpst, 1000, 450)

# Input for scores and calculation of net scores
st.subheader("Enter Your Score")
net_scores = {}

for golfer in snpst.index:
    score = st.number_input(f"Enter score for {golfer}:", min_value=0, max_value=200, step=1)
    championship_hc = snpst.at[golfer, "Championship HC"]
    net_score = score - championship_hc
    net_scores[golfer] = net_score

# Display and rank players by net score
if st.button("Calculate Rankings"):
    net_scores_df = pd.DataFrame(list(net_scores.items()), columns=["Golfer", "Net Score"])
    net_scores_df = net_scores_df.sort_values(by="Net Score")

    # Add rank labels
    net_scores_df['Rank'] = range(1, len(net_scores_df) + 1)
    net_scores_df['Label'] = net_scores_df['Rank'].apply(lambda x: 
                                                         "First" if x == 1 else 
                                                         "Second" if x == 2 else 
                                                         "Third" if x == 3 else 
                                                         f"{x}th")

    # Display rankings
    st.subheader("Rankings")
    st.dataframe(net_scores_df[['Golfer', 'Net Score', 'Label']])
