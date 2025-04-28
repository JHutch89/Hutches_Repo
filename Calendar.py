import streamlit as st
import calendar
import datetime
import pandas as pd
import plotly.graph_objects as go
from datetime import timedelta
import random

# Set page configuration
st.set_page_config(
    page_title="Interactive Calendar",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .calendar-day {
        border: 1px solid #ddd;
        padding: 10px;
        text-align: center;
        height: 80px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .calendar-day:hover {
        background-color: #f0f0f0;
    }
    .calendar-header {
        background-color: #4e8df5;
        color: white;
        padding: 10px;
        text-align: center;
        font-weight: bold;
    }
    .today {
        background-color: #e7f0fe;
        font-weight: bold;
    }
    .event-dot {
        height: 10px;
        width: 10px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 3px;
    }
    .main-header {
        text-align: center;
        font-size: 2.5rem;
        color: #4e8df5;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 class='main-header'>Interactive Calendar</h1>", unsafe_allow_html=True)

# Initialize session state to store events
if 'events' not in st.session_state:
    st.session_state.events = {}

if 'selected_date' not in st.session_state:
    st.session_state.selected_date = datetime.date.today()

# Sidebar for controls
with st.sidebar:
    st.header("Calendar Controls")
    
    # Date selection
    current_year = st.session_state.selected_date.year
    current_month = st.session_state.selected_date.month
    
    # Month and year selection
    col1, col2 = st.columns(2)
    with col1:
        month = st.selectbox("Month", list(range(1, 13)), index=current_month-1)
    with col2:
        year = st.selectbox("Year", list(range(2020, 2031)), index=current_year-2020)
    
    # Update the selected date when month/year changes
    if month != current_month or year != current_year:
        st.session_state.selected_date = datetime.date(year, month, 1)
    
    # Navigation buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("◀ Previous"):
            # Go to previous month
            first_day = datetime.date(st.session_state.selected_date.year, st.session_state.selected_date.month, 1)
            prev_month = first_day - timedelta(days=1)
            st.session_state.selected_date = datetime.date(prev_month.year, prev_month.month, 1)
            st.rerun()
    
    with col2:
        if st.button("Today"):
            st.session_state.selected_date = datetime.date.today()
            st.rerun()
    
    with col3:
        if st.button("Next ▶"):
            # Go to next month
            if st.session_state.selected_date.month == 12:
                st.session_state.selected_date = datetime.date(st.session_state.selected_date.year + 1, 1, 1)
            else:
                st.session_state.selected_date = datetime.date(st.session_state.selected_date.year, st.session_state.selected_date.month + 1, 1)
            st.rerun()
    
    # Add event form
    st.header("Add New Event")
    event_date = st.date_input("Event Date", datetime.date.today())
    event_title = st.text_input("Event Title")
    event_description = st.text_area("Event Description")
    event_color = st.color_picker("Event Color", "#4e8df5")
    
    if st.button("Add Event"):
        date_key = event_date.isoformat()
        if date_key not in st.session_state.events:
            st.session_state.events[date_key] = []
        
        st.session_state.events[date_key].append({
            "title": event_title,
            "description": event_description,
            "color": event_color
        })
        st.success(f"Added event '{event_title}' on {event_date.strftime('%B %d, %Y')}")
    
    # Sample data generation
    if st.button("Add Sample Events"):
        # Clear existing events
        st.session_state.events = {}
        
        # Generate random events for the current month
        current_date = datetime.date(year, month, 1)
        for _ in range(10):
            random_day = random.randint(1, calendar.monthrange(year, month)[1])
            event_date = datetime.date(year, month, random_day)
            date_key = event_date.isoformat()
            
            if date_key not in st.session_state.events:
                st.session_state.events[date_key] = []
            
            colors = ["#4e8df5", "#f54e4e", "#4ef58f", "#f5a74e", "#a74ef5"]
            event_types = ["Meeting", "Appointment", "Reminder", "Birthday", "Holiday"]
            
            random_index = random.randint(0, len(event_types) - 1)
            st.session_state.events[date_key].append({
                "title": f"{event_types[random_index]} {random.randint(1, 100)}",
                "description": f"This is a sample {event_types[random_index].lower()}",
                "color": colors[random_index]
            })
        
        st.success("Added sample events for the current month")

# Main area - Calendar display
selected_year = st.session_state.selected_date.year
selected_month = st.session_state.selected_date.month
today = datetime.date.today()

# Get the calendar for the selected month
cal = calendar.monthcalendar(selected_year, selected_month)
month_name = calendar.month_name[selected_month]

# Display month and year
st.markdown(f"<h2 style='text-align: center;'>{month_name} {selected_year}</h2>", unsafe_allow_html=True)

# Create calendar grid with columns for each day of the week
cols = st.columns(7)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Display day headers
for i, day in enumerate(days):
    cols[i].markdown(f"<div class='calendar-header'>{day}</div>", unsafe_allow_html=True)

# Display calendar days
for week in cal:
    cols = st.columns(7)
    for i, day in enumerate(week):
        if day == 0:
            # Empty cell for days not in the month
            cols[i].markdown("<div class='calendar-day' style='color: #ccc;'></div>", unsafe_allow_html=True)
        else:
            # Create a date object for this day
            current_date = datetime.date(selected_year, selected_month, day)
            date_key = current_date.isoformat()
            
            # Check if there are events for this day
            has_events = date_key in st.session_state.events
            events_html = ""
            
            if has_events:
                for event in st.session_state.events[date_key]:
                    events_html += f"<span class='event-dot' style='background-color: {event['color']};'></span>"
            
            # Check if this is today
            is_today = (current_date == today)
            today_class = " today" if is_today else ""
            
            # Display the day with any events
            with cols[i]:
                day_html = f"""
                <div class='calendar-day{today_class}' id='day-{day}'>
                    <div style='font-size: 1.2rem;'>{day}</div>
                    <div>{events_html}</div>
                </div>
                """
                st.markdown(day_html, unsafe_allow_html=True)
                
                # If clicked, show events for this day
                if st.button(f"View {day}", key=f"btn-{day}", use_container_width=True):
                    st.session_state.selected_date = current_date
                    
# Event details section for selected date
st.markdown("---")
selected_date_fmt = st.session_state.selected_date.strftime("%B %d, %Y")
st.markdown(f"## Events for {selected_date_fmt}")

date_key = st.session_state.selected_date.isoformat()
if date_key in st.session_state.events and st.session_state.events[date_key]:
    for i, event in enumerate(st.session_state.events[date_key]):
        with st.expander(f"{event['title']}", expanded=True):
            st.markdown(f"<div style='border-left: 5px solid {event['color']}; padding-left: 10px;'>", unsafe_allow_html=True)
            st.write(f"**Description:** {event['description']}")
            
            # Delete button for this event
            if st.button("Delete Event", key=f"delete-{i}"):
                st.session_state.events[date_key].remove(event)
                if not st.session_state.events[date_key]:
                    st.session_state.events.pop(date_key)
                st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info(f"No events scheduled for {selected_date_fmt}")

# Analytics Section
st.markdown("---")
st.header("Calendar Analytics")

# Only show analytics if there are events
if st.session_state.events:
    # Prepare data for visualizations
    event_counts = {}
    for date_key, events in st.session_state.events.items():
        date_obj = datetime.date.fromisoformat(date_key)
        month_year = date_obj.strftime("%B %Y")
        
        if month_year not in event_counts:
            event_counts[month_year] = 0
        event_counts[month_year] += len(events)
    
    # Create DataFrame for visualization
    df = pd.DataFrame({
        'Month': list(event_counts.keys()),
        'Events': list(event_counts.values())
    })
    
    # Create a bar chart
    fig = go.Figure(data=[
        go.Bar(x=df['Month'], y=df['Events'], marker_color='#4e8df5')
    ])
    
    fig.update_layout(
        title="Events by Month",
        xaxis_title="Month",
        yaxis_title="Number of Events",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Event Type Distribution (if we had categories)
    st.subheader("Event Distribution")
    
    # Count events by day of week
    weekday_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for date_key in st.session_state.events:
        date_obj = datetime.date.fromisoformat(date_key)
        weekday = date_obj.weekday()
        weekday_counts[weekday] += len(st.session_state.events[date_key])
    
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_df = pd.DataFrame({
        'Day': weekday_names,
        'Events': [weekday_counts[i] for i in range(7)]
    })
    
    # Create a pie chart
    fig = go.Figure(data=[
        go.Pie(
            labels=weekday_df['Day'],
            values=weekday_df['Events'],
            hole=.3,
            marker_colors=['#4e8df5', '#f54e4e', '#4ef58f', '#f5a74e', '#a74ef5', '#f5e14e', '#4ef5e1']
        )
    ])
    
    fig.update_layout(title="Events by Day of Week", height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Display upcoming events
    st.subheader("Upcoming Events")
    upcoming_events = []
    today = datetime.date.today()
    
    for date_key, events in st.session_state.events.items():
        date_obj = datetime.date.fromisoformat(date_key)
        if date_obj >= today:
            for event in events:
                upcoming_events.append({
                    "date": date_obj,
                    "title": event["title"],
                    "description": event["description"],
                    "color": event["color"]
                })
    
    # Sort by date
    upcoming_events.sort(key=lambda x: x["date"])
    
    # Display the next 5 events
    if upcoming_events:
        for i, event in enumerate(upcoming_events[:5]):
            st.markdown(
                f"""
                <div style='padding: 10px; margin-bottom: 10px; border-left: 5px solid {event["color"]}; background-color: #f9f9f9;'>
                    <div style='font-weight: bold;'>{event["title"]}</div>
                    <div style='color: #666;'>{event["date"].strftime("%B %d, %Y")}</div>
                    <div>{event["description"]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("No upcoming events")
else:
    st.info("Add some events to view analytics")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 20px;'>
        Interactive Calendar App | Built with Streamlit
    </div>
    """,
    unsafe_allow_html=True
)