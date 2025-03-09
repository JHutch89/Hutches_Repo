import pandas as pd
import streamlit as st
from datetime import datetime

# Set up tournament calendar
calendar = [
    ["4/12/25", "Pinelands", "TBD", "$TBD"],
    ["5/17/25", "Rancocas", "TBD", "$TBD"],
    ["6/14/25", "Mercer Oaks", "TBD", "$TBD"],
    ["7/19/25", "Town and Country", "TBD", "$TBD"],
    ["8/23/25", "Cream Ridge", "TBD", "$TBD"],
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
    ["Jason Hutches", "$120", "23"],
    ["Dave Cunningham", "$150", "23"],
    ["Alex Taraschi", "$150", "21.9"],
    ["Ken Cooper", "$150", "31.6"],
    ["Chick Campbell", "$100", "36.3"],
    ["Tom Taraschi", "$150", "28.8"],
    ["Rich Hamner", "$80", "26.8"],
    ["Shawn Frick", "$120", "28.3"],
    ["Mark McDermott", "$150", "27.2"],
    ["Don Latka", "$150", "28.1"]
]

snpst = pd.DataFrame(member_snpsht, columns=["Golfer", "Dues Owed", "HC"])
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
