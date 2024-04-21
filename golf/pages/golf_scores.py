import pandas as pd
import streamlit as st

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Load and prepare the data
sjmga_2023 = pd.read_csv("golf/pages/sjmga_2023.csv", dtype={"Long Drive": str, "Closest Pin": str})
sjmga_2023 = sjmga_2023.fillna("")
sjmga_2023['Course Date'] = pd.to_date(sjmga_2023['Course Date'],format='%m/%d/%y')
sjmga_2023['Course Date'] = sjmga_2023['Course Date'].dt.date
sjmga_2023['Year'] = sjmga_2023['Course Date'].dt.year.astype(str)
sjmga_2023.set_index("Golfer", inplace=True)
sjmga_2023.loc[sjmga_2023["Outing"] == "Makefield Highlands", "Course Score"] *= 2

st.title("SJMGA Scores | Handicaps | Winnings")
image_path = "golf/pages/golf_earnings.jpeg"
st.image(image_path, width=250)

st.write("## Filters")

# Year radio buttons
year_options = ["All"] + sorted(sjmga_2023['Year'].unique().tolist())
year_option = st.radio("Select Year", year_options, index=0)

# Golfer filter
unique_golfers = sorted(sjmga_2023.index.unique())
selected_golfer = st.selectbox("Select Golfer", ["All"] + unique_golfers)

# Course selection with "All Courses" option
unique_courses = ["All Courses"] + sorted(sjmga_2023['Outing'].unique().tolist())
selected_course = st.selectbox("Select Course", unique_courses, index=0)

# Score slider
min_score, max_score = int(sjmga_2023['Course Score'].min()), int(sjmga_2023['Course Score'].max())
selected_score_range = st.slider("Select Score Range", min_score, max_score, (min_score, max_score))

# Apply filters directly to sjmga_2023
if year_option != "All":
    sjmga_2023 = sjmga_2023[sjmga_2023['Year'] == year_option]
if selected_golfer != "All":
    sjmga_2023 = sjmga_2023.loc[[selected_golfer]]
if selected_course != "All Courses":
    sjmga_2023 = sjmga_2023[sjmga_2023['Outing'] == selected_course]
sjmga_2023 = sjmga_2023[
    (sjmga_2023['Course Score'] >= selected_score_range[0]) &
    (sjmga_2023['Course Score'] <= selected_score_range[1])
]

# Calculate and display the average score for the visible dataset
if not sjmga_2023.empty:
    average_score_visible = round(sjmga_2023['Course Score'].mean(), 0)
    st.write(f"Average Score for Visible Data: {average_score_visible}")
else:
    st.write("No data matches your filters.")

# Display the original DataFrame after filtering
st.dataframe(sjmga_2023, 5000, None)
