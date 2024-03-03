import streamlit as st

st.title("SJMGA Home")
image_path = "golf_logo.jpg"
st.image(image_path, width=400)

st.write("")
st.write("Welcome to the SJMGA app home page! Please click one of the links below to navigate to your desired destination. If you run into any issues, please reach out to Jason Hutches.")

# Link to golf_cal.py
st.page_link('golf_cal.py', label= "Schedule | Dues")

# Link to golf_app.py
st.page_link( 'golf_app.py', label= "Scores | Handicaps | Winnings")