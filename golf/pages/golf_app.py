import pandas as pd
import streamlit as st

def run():
    # Load and prepare the data
    sjmga_2023 = pd.read_csv("sjmga_2023.csv", dtype={"Long Drive": str, "Closest Pin": str})
    sjmga_2023 = sjmga_2023.fillna("")
    # Convert 'Course Date' to datetime and extract the year as a string
    sjmga_2023['Course Date'] = pd.to_datetime(sjmga_2023['Course Date'])
    sjmga_2023['Year'] = sjmga_2023['Course Date'].dt.year.astype(str)
    sjmga_2023.set_index("Golfer", inplace=True)

    # Double the "Course Score" for "Makefield Highlands"
    sjmga_2023.loc[sjmga_2023["Outing"] == "Makefield Highlands", "Course Score"] *= 2

    # # Streamlit App setup
    # image_path = "Golf App/golf_logo.jpg"
    # st.image(image_path, use_column_width=True, width=250)

    # Sidebar for filters
    with st.sidebar:
        st.write("## Filters")

        # Year radio buttons
        year_options = ["All"] + sorted(sjmga_2023['Year'].unique().tolist())
        year_option = st.radio("Select Year", year_options, index=0)

        # Golfer filter
        unique_golfers = sorted(sjmga_2023.index.unique())
        selected_golfer = st.selectbox("Select Golfer", ["All"] + unique_golfers)

        # Course selection with "All Courses" option
        unique_courses = ["All Courses"] + sorted(sjmga_2023['Outing'].unique().tolist())
        selected_course = st.selectbox("Select Course", unique_courses, index=0)  # Single select with "All Courses"

        # Score slider
        min_score, max_score = int(sjmga_2023['Course Score'].min()), int(sjmga_2023['Course Score'].max())
        selected_score_range = st.slider("Select Score Range", min_score, max_score, (min_score, max_score))

    # Filtering logic
    filtered_data = sjmga_2023.copy()

    # Filter by year if not "All"
    if year_option != "All":
        filtered_data = filtered_data[filtered_data['Year'] == year_option]

    # Filter by golfer if not "All"
    if selected_golfer != "All":
        filtered_data = filtered_data.loc[[selected_golfer]]

    # Apply course filter if not "All Courses"
    if selected_course != "All Courses":
        filtered_data = filtered_data[filtered_data['Outing'] == selected_course]

    # Further filter by score
    filtered_data = filtered_data[
        (filtered_data['Course Score'] >= selected_score_range[0]) &
        (filtered_data['Course Score'] <= selected_score_range[1])
    ]

    # Calculate and display the average score for the visible dataset
    if not filtered_data.empty:
        average_score_visible = round(filtered_data['Course Score'].mean(), 0)
        st.write(f"Average Score for Visible Data: {average_score_visible}")
    else:
        st.write("No data matches your filters.")

    # Display the filtered DataFrame
    st.dataframe(filtered_data.reset_index())
