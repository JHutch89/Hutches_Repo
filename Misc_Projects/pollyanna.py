import streamlit as st
import pandas as pd
import time

# Sample data
data = {
    'buyer_name': ['Jason', 'Steve', 'Katie', 'Brittan', 'Courtney', 'Bryan', 'Alec',],
    'buys_for_name': ['Steve', 'Courtney', 'Bryan', 'Jason', 'Katie', 'Alec', 'Brittan']
}

# Create a DataFrame
df = pd.DataFrame(data)

def spin_wheel(df, selected_name):
    # Custom CSS to center the header
    st.markdown(
        """
        <style>
        .header {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="header">2024 Christmas Pollyanna</h1>', unsafe_allow_html=True)

    # Display the centered image at the top
    st.image("Misc_Projects/Images/santa.jpeg", width=350)
    st.write("")
    st.write("Choose your name from the dropdown:")
    
    # Dropdown to let the user choose their name
    if selected_name is None:
        selected_name = st.selectbox("Select your name", df['buyer_name'])
        
    st.write("")
    st.write("Click 'Spin' to generate your 2024 Pollyanna assignment!")

    # Check if the user has selected a name
    if selected_name:
        # Get the corresponding name they are buying for
        buys_for_name = df.loc[df['buyer_name'] == selected_name, 'buys_for_name'].values[0]

        # Create a button to trigger the spinning animation
        if st.button("Spin"):
            with st.spinner("Spinning..."):
                # Simulate spinning for a few seconds
                time.sleep(3)

                # Display the result
                st.success(f"This Christmas {selected_name} is buying for {buys_for_name}!")

# Call the function to create the spinning wheel
spin_wheel(df, selected_name=None)
