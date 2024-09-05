import streamlit as st

st.image("JHutches_Portfolio/Hutches_Photo.jpeg", width=200)

st.title("Jason Hutches' Portfolio")

# About Me section
st.header("Get to Know Me...")
st.write("""
Hi!  I'm Jason Hutches, proud father of two wonderful children and husband to the most amazing wife. I'm a data scientist/analyst by trade, but 
off the clock you'll find me coaching my daughter's soccer team, running a golf league and spending time with family.
I'm a huge soccer and hockey fan (go Chelsea and Devils!), and enjoy sharing that enthusiasm with my kids.
I have a deep passion for math and data, and I am always on the lookout for new ways to learn, grow and apply that knowledge.
Every day is a chance to connect the dots—whether in data or in life—and I’m here for the ride!
         """)  

# Professional Summary
st.header("Professional Summary")
professional_summary = """
Accomplished data professional with over 10 years of experience in analytics, data science, 
and business intelligence. Proven track record in developing and implementing comprehensive 
BI solutions and strategic plans, driving business success. Skilled in mentoring and developing 
high-performing teams and effectively communicating strategic insights to stakeholders. Experienced 
in Agile delivery and program management.
"""
st.write(professional_summary)

st.header("Download My Resume")
with open("JHutches_Portfolio/Jason Hutches Resume.docx", "rb") as file:
    btn = st.download_button(
        label="Download Resume",
        data=file,
        file_name="Jason_Hutches_Resume.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")