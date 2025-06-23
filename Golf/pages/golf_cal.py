import pandas as pd
import streamlit as st
from datetime import datetime

# Set up tournament calendar
calendar = [
    ["5/17/25", "Rancocas", "8:20am", "$92"],
    ["6/14/25", "Hanover", "8:26am", "$70"],
    ["7/19/25", "Town and Country", "TBD", "$TBD"],
    ["8/23/25", "Cream Ridge", "TBD", "$TBD"],
    ["9/6/25", "Pinelands", "TBD", "$95"],
    ["9/20/25", "Buena Vista", "TBD", "$TBD"],
    ["10/11/25", "Golden Pheasant", "TBD", "$TBD"],
    ["11/1/25", "TBD", "TBD", "$TBD"]
]

sjmga_2025 = pd.DataFrame(calendar, columns=["Date", "Course", "Time", "Price"])
sjmga_2025['Date'] = pd.to_datetime(sjmga_2025['Date'], format='%m/%d/%y')
sjmga_2025['Date'] = sjmga_2025['Date'].dt.date
sjmga_2025.set_index("Date", inplace=True)

# Set up golfer data
member_snpsht = [
    ["Jason Hutches", "Paid", "$15", "21.7"],
    ["Dave Cunningham", "Paid", "$10", "21.8"],
    ["Alex Taraschi", "Paid", "$45", "20.8"],
    ["Ken Cooper", "Paid", "$10", "30.7"],
    ["Chick Campbell", "Paid", "$15", "36.2"],
    ["Tom Taraschi", "Paid", "$0", "28.8"],
    ["Rich Hamner", "Paid", "$35", "25.8"],
    ["Shawn Frick", "$120", "$0", "28.8"],
    ["Mark McDermott", "Paid", "$55", "25.3"],
    ["Don Latka", "Paid", "$5", "27.5"]
]

snpst = pd.DataFrame(member_snpsht, columns=["Golfer", "Dues Owed", "Winnings", "HC"])
snpst = snpst.sort_values(by='Golfer')
snpst.set_index("Golfer", inplace=True)

# Streamlit App setup
st.title("SJMGA 2025 Schedule | League Dues")
image_path = "Golf/pages/golf_cal.jpg"
st.image(image_path, width=300)

# Display calendar and golfer data
st.write("SJMGA 2025 Schedule")
st.dataframe(sjmga_2025, 500, None)
st.write("")
st.write("")
st.write("SJMGA 2025 Snapshot")
st.dataframe(snpst, 1000, 450)


## Championship Score Calculation Block
# # Input for scores and calculation of net scores
# st.subheader("Enter Your Score")
# net_scores = {}
# for golfer in snpst.index:
#     score = st.number_input(f"Enter score for {golfer}:", min_value=0, max_value=200, step=1)
#     championship_hc = snpst.at[golfer, "Championship HC"]
#     net_score = score - championship_hc
#     net_scores[golfer] = net_score

# # Display and rank players by net score
# if st.button("Calculate Rankings"):
#     net_scores_df = pd.DataFrame(list(net_scores.items()), columns=["Golfer", "Net Score"])
#     net_scores_df = net_scores_df.sort_values(by="Net Score")

#     # Add rank labels
#     net_scores_df['Rank'] = range(1, len(net_scores_df) + 1)
#     net_scores_df['Label'] = net_scores_df['Rank'].apply(lambda x: 
#                                                          "First" if x == 1 else 
#                                                          "Second" if x == 2 else 
#                                                          "Third" if x == 3 else 
#                                                          f"{x}th")

#     # Display rankings
#     st.subheader("Rankings")
#     st.dataframe(net_scores_df[['Golfer', 'Net Score', 'Label']])
