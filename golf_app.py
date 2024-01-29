import pandas as pd
import streamlit as st

sjmga_2023 = pd.read_csv("sjmga_2023.csv")
sjmga_2023 = sjmga_2023.fillna("")
sjmga_2023.set_index("Golfer", inplace=True)

# Streamlit App
st.title("South Jersey Men's Golf Association")

image_path = "golf_logo.jpg"
image = Image.open(image_path)

# Resize the image to the desired width and height
desired_width = 400
desired_height = 400 
image = image.resize((desired_width, desired_height))

# Center and display the image using Markdown
st.markdown("<div style='text-align: center'>", unsafe_allow_html=True)
st.image(image, width=desired_width)
st.markdown("</div>", unsafe_allow_html=True)

# Get unique golfers from the index
unique_golfers = sorted(sjmga_2023.index.unique())

# Create a dropdown for selecting a golfer
selected_golfer = st.selectbox("Select Golfer", unique_golfers)

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

