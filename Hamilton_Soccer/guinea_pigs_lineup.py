import streamlit as st
import matplotlib.pyplot as plt
import json
import os

# File to save player assignments
save_file = 'player_assignments.json'

# Load player assignments if file exists
if os.path.exists(save_file):
    with open(save_file, 'r') as f:
        saved_assignments = json.load(f)
else:
    saved_assignments = {}

# Soccer field layout using matplotlib
def draw_soccer_field(team1_def_left, team1_def_right, team1_off_left, team1_off_center, team1_off_right,
                      team2_def_left, team2_def_right, team2_off_left, team2_off_center, team2_off_right):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim([0, 100])
    ax.set_ylim([0, 60])
    
    # Set the field background color to light green
    ax.set_facecolor('lightgreen')
    
    # Field borders and midline
    plt.plot([0, 100], [0, 0], color="black")  # Bottom line
    plt.plot([0, 100], [60, 60], color="black")  # Top line
    plt.plot([0, 0], [0, 60], color="black")  # Left line
    plt.plot([100, 100], [0, 60], color="black")  # Right line
    plt.plot([50, 50], [0, 60], color="black")  # Midline

    # Center circle
    center_circle = plt.Circle((50, 30), 9.15, color="black", fill=False)
    ax.add_artist(center_circle)

    # Goals
    plt.plot([0, 0], [22.5, 37.5], color="black", linewidth=5)  # Left goal
    plt.plot([100, 100], [22.5, 37.5], color="black", linewidth=5)  # Right goal

    # Adding Team 1 (left side) with bold text
    ax.text(10, 25, team1_def_left, fontsize=12, ha='center', color='blue', weight='bold')  # Team 1 Left Defender
    ax.text(10, 35, team1_def_right, fontsize=12, ha='center', color='blue', weight='bold')  # Team 1 Right Defender
    ax.text(35, 20, team1_off_left, fontsize=12, ha='center', color='blue', weight='bold')  # Team 1 Left Offense
    ax.text(35, 30, team1_off_center, fontsize=12, ha='center', color='blue', weight='bold')  # Team 1 Center Offense
    ax.text(35, 40, team1_off_right, fontsize=12, ha='center', color='blue', weight='bold')  # Team 1 Right Offense

    # Adding Team 2 (right side) with bold text
    ax.text(90, 25, team2_def_left, fontsize=12, ha='center', color='red', weight='bold')  # Team 2 Left Defender
    ax.text(90, 35, team2_def_right, fontsize=12, ha='center', color='red', weight='bold')  # Team 2 Right Defender
    ax.text(65, 20, team2_off_left, fontsize=12, ha='center', color='red', weight='bold')  # Team 2 Left Offense
    ax.text(65, 30, team2_off_center, fontsize=12, ha='center', color='red', weight='bold')  # Team 2 Center Offense
    ax.text(65, 40, team2_off_right, fontsize=12, ha='center', color='red', weight='bold')  # Team 2 Right Offense

    ax.axis("off")  # Hide the axis
    return fig

# Player list
players = [
    'Ada M.', 
    'Adriana M.', 
    'Avery W.', 
    'Demi F.', 
    'Harper H.', 
    'Isabella A.', 
    'Jade M.', 
    'Maelie T.',
    'Olivia K.',
    'Zoey A.'
]

# Retrieve saved player selections or use defaults
team1_def_left = saved_assignments.get("team1_ld", players[0])
team1_def_right = saved_assignments.get("team1_rd", players[1])
team1_off_left = saved_assignments.get("team1_lo", players[2])
team1_off_center = saved_assignments.get("team1_co", players[3])
team1_off_right = saved_assignments.get("team1_ro", players[4])
team2_def_left = saved_assignments.get("team2_ld", players[5])
team2_def_right = saved_assignments.get("team2_rd", players[6])
team2_off_left = saved_assignments.get("team2_lo", players[7])
team2_off_center = saved_assignments.get("team2_co", players[8])
team2_off_right = saved_assignments.get("team2_ro", players[9])

# Team Positioning with two columns
st.title("5v5 Soccer Team Positioning")

col1, col2 = st.columns(2)

# Team 1 (Left side of the field)
with col1:
    st.header("Team 1")
    st.subheader("Defense")
    team1_def_left = st.selectbox("Left Defender", players, index=players.index(team1_def_left), key="team1_ld")
    team1_def_right = st.selectbox("Right Defender", players, index=players.index(team1_def_right), key="team1_rd")
    
    st.subheader("Offense")
    team1_off_left = st.selectbox("Left Offense", players, index=players.index(team1_off_left), key="team1_lo")
    team1_off_center = st.selectbox("Center Offense", players, index=players.index(team1_off_center), key="team1_co")
    team1_off_right = st.selectbox("Right Offense", players, index=players.index(team1_off_right), key="team1_ro")

# Team 2 (Right side of the field)
with col2:
    st.header("Team 2")
    st.subheader("Defense")
    team2_def_left = st.selectbox("Left Defender", players, index=players.index(team2_def_left), key="team2_ld")
    team2_def_right = st.selectbox("Right Defender", players, index=players.index(team2_def_right), key="team2_rd")
    
    st.subheader("Offense")
    team2_off_left = st.selectbox("Left Offense", players, index=players.index(team2_off_left), key="team2_lo")
    team2_off_center = st.selectbox("Center Offense", players, index=players.index(team2_off_center), key="team2_co")
    team2_off_right = st.selectbox("Right Offense", players, index=players.index(team2_off_right), key="team2_ro")

# Draw the field and display player names
st.pyplot(draw_soccer_field(team1_def_left, team1_def_right, team1_off_left, team1_off_center, team1_off_right,
                            team2_def_left, team2_def_right, team2_off_left, team2_off_center, team2_off_right))

# Save player assignments to JSON when the app reruns
save_data = {
    "team1_ld": team1_def_left,
    "team1_rd": team1_def_right,
    "team1_lo": team1_off_left,
    "team1_co": team1_off_center,
    "team1_ro": team1_off_right,
    "team2_ld": team2_def_left,
    "team2_rd": team2_def_right,
    "team2_lo": team2_off_left,
    "team2_co": team2_off_center,
    "team2_ro": team2_off_right,
}

with open(save_file, 'w') as f:
    json.dump(save_data, f)
