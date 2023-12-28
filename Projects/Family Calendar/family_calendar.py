import streamlit as st
import json
from datetime import date
from collections import defaultdict

def load_events():
    try:
        with open("events.json", "r") as file:
            events = json.load(file)
    except FileNotFoundError:
        events = defaultdict(list)
    return events

def save_events(events):
    with open("events.json", "w") as file:
        json.dump(events, file, indent=2)

# Load existing events from a file
events = load_events()

# Streamlit UI
st.title("Monthly Events Organizer")

# User input for adding events
selected_date = st.date_input("Select a date", date.today())
event_time = st.text_input("Event time (e.g., 18:00)", "12:00")
event_description = st.text_input("Event description")

# Debug prints
st.write(f"Selected Date: {selected_date}")
st.write(f"Event Time: {event_time}")
st.write(f"Event Description: {event_description}")

# Add event
if st.button("Add Event"):
    month_key = f"{selected_date.strftime('%B')} {selected_date.year}"
    st.write(f"Month Key: {month_key}")

    # Ensure the month_key exists in events
    events[month_key].append({"day": selected_date.day, "time": event_time, "event": event_description})
    save_events(events)

    # Debug print
    st.write(f"After Update - Events: {events}")

# Delete event
if st.button("Delete Event"):
    selected_event_month = st.selectbox("Select the month", list(events.keys()))
    events_for_month = events.get(selected_event_month, [])
    if events_for_month:
        st.subheader(f"Events for {selected_event_month}:")
        for i, event in enumerate(events_for_month):
            st.write(f"{i + 1}. Day {event['day']} at {event['time']} - {event['event']}")

        event_to_delete = st.number_input("Enter the event number to delete", min_value=1, max_value=len(events_for_month), step=1)
        if st.button("Confirm Deletion"):
            # Delete the selected event
            events[selected_event_month].pop(event_to_delete - 1)
            save_events(events)

# Display events for the selected month
if events:
    st.subheader("Display Events for a Specific Month")
    selected_display_month = st.selectbox("Select the month to display events", list(events.keys()))
    events_for_display_month = events.get(selected_display_month, [])
    for i, event in enumerate(events_for_display_month):
        st.write(f"{i + 1}. Day {event['day']} at {event['time']} - {event['event']}")
