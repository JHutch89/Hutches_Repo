import streamlit as st

st.image("Hutches_Folio/Hutches_Photo.jpeg", width=200)

st.title("Jason Hutches Portfolio")

# About Me section
st.header("Get to Know Me...")
st.write("""
"Hi!  I'm Jason Hutches, father of two wonderful children and husband to the most amazing wife. I'm a data data scientist by trade, but 
 off the clock you'll find me coaching my daughter's soccer team, operating a golf league and spending time with family.
   I'm a huge soccer and hockey fan (go Chelsea and Devils!), and enjoy sharing that passion with my kids.
 I have a deep enthusiasm for math/data and am always eager to expand my knowledge. Life is good, and every day presents a new opportunity to learn and grow!"
         """)  

# Professional Summary
st.header("Professional Summary")
professional_summary = """
Accomplished Data Analytics professional with over a decade of experience in managing teams and enhancing operational processes across diverse industries including eCommerce, logistics, client relations, and compliance. 
Expert in leveraging statistical models and data to drive strategic growth and operational excellence. Known for a robust ability to swiftly adapt, master, and implement solutions that consistently achieve improved business outcomes.
"""
st.write(professional_summary)

# Placeholder buttons for other pages
st.header("My Work")
st.button("Project 1 (Placeholder)")
st.button("Project 2 (Placeholder)")
st.button("Project 3 (Placeholder)")

st.header("Download My Resume")
with open("Hutches_Folio/Jason Hutches Resume.docx", "rb") as file:
    btn = st.download_button(
        label="Download Resume",
        data=file,
        file_name="Jason_Hutches_Resume.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")