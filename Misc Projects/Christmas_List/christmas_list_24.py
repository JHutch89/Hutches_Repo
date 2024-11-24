import streamlit as st
import pandas as pd
import os

# Absolute file path to store data
file_path = "/Users/jasonhutches/Hutches_Repo/Misc Projects/Christmas_List/christmas_list.csv"

# Load or initialize data
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    data = pd.DataFrame(columns=["Child", "Item", "Cost", "Purchased"])

# Ensure proper data types
data["Cost"] = pd.to_numeric(data["Cost"], errors="coerce")
data["Purchased"] = data["Purchased"].astype(bool)

# Christmas theme
st.set_page_config(page_title="Christmas Wish List", page_icon="🎄", layout="centered")
st.markdown("<h1 style='text-align: center; color: red;'>🎅 Harper and Miles' Christmas List 🎁</h1>", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.markdown("🎄 **Navigation**")
view_mode = st.sidebar.radio("Select Child:", ("Harper", "Miles"))

# Filter data for the selected child
filtered_data = data[data["Child"] == view_mode]

# Main app
st.subheader(f"🎁 {view_mode}'s Wish List")

# Show current list
if not filtered_data.empty:
    st.write("### Current List:")
    formatted_data = filtered_data.copy()
    formatted_data["Cost"] = formatted_data["Cost"].apply(lambda x: f"${x:.2f}")
    st.table(formatted_data[["Item", "Cost", "Purchased"]])
else:
    st.write(f"No items in {view_mode}'s list yet. Add some below!")

# Add new items
st.subheader("Add a New Item")
with st.form(key="add_item_form", clear_on_submit=True):
    item = st.text_input("Item Name", key="item_input")
    cost = st.number_input("Cost", min_value=0.0, format="%.2f", key="cost_input")
    add_item_button = st.form_submit_button("Add to List")

if add_item_button:
    if item.strip():  # Prevent empty items
        new_entry = {"Child": view_mode, "Item": item, "Cost": cost, "Purchased": False}
        data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
        st.success(f"Added '{item}' to {view_mode}'s list!")
    else:
        st.error("Please enter an item name.")

# Save data
if st.button("Save Changes"):
    try:
        st.write("Saving data...")  # Debug message
        st.write(data)  # Debug: display current dataframe
        data.to_csv(file_path, index=False)
        st.success("Changes saved successfully!")
    except Exception as e:
        st.error(f"Error saving file: {e}")

# Display footer
st.markdown("<footer style='text-align: center; margin-top: 50px;'>🎄 Merry Christmas from Harper and Miles! 🎅</footer>", unsafe_allow_html=True)
