import pandas as pd
import streamlit as st

sjmga_2023 = pd.read_csv("/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/Projects/Golf App/CSV/sjmga_2023.csv")
sjmga_2023 = sjmga_2023.fillna("")
sjmga_2023.set_index("Golfer", inplace=True)

# Streamlit App
st.title("SJMGA 2023")

image_path = "Projects/Golf App/Images/golf ball hole.jpeg"
st.image(image_path, use_column_width=True)

# Create a dropdown for selecting a golfer
selected_golfer = st.selectbox("Select Golfer", sjmga_2023.index)

# Filter the DataFrame based on the selected golfer
filtered_data = sjmga_2023.loc[selected_golfer]
filtered_data = filtered_data.drop(columns=["Index"])
# Double the "Course Score" where "Course" is "Makefield Highlands"
filtered_data.loc[filtered_data["Outing"] == "Makefield Highlands", "Course Score"] *= 2

# Calculate and display the average score for the selected golfer
average_score = round(filtered_data['Course Score'].mean(),0)
st.write(f"Average Score for {selected_golfer}: {average_score}")

# Display the filtered data
st.write("Selected Golfer:", selected_golfer)
st.write(filtered_data)

