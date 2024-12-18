import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px
import streamlit as st

# Load your NFL 2023 data
nfl_data = pd.read_csv('NFL_Clustering/CSV Source/nfl_2023_offense.csv') 

st.title("2023 NFL Player Clustering: KMeans")
st.image('NFL_Clustering/Images/football_data.jpeg', width=350)

# Define a function to create clustering model, visualize it, and save cluster stats
def cluster_and_visualize(nfl_data, position):
    # Filter data to include only players of the selected position
    nfl_data_position = nfl_data[nfl_data['position'] == position].copy() 

    # Feature selection based on position using actual column names
    if position == "QB":
        features = nfl_data_position[['completions', 'attempts', 'passing_yards', 'passing_first_down', 'passing_tds', 'interceptions', 'sack_fumbles', 'total_yards']].dropna()
    elif position == "RB":
        features = nfl_data_position[['rushing_yards', 'rushing_tds', 'total_yards', 'rushing_first_downs', 'rushing_fumbles', 'receiving_yards', 'receptions']].dropna()
    elif position == "WR":
        features = nfl_data_position[['receptions', 'receiving_yards', 'receiving_tds', 'receiving_first_downs', 'receiving_fumbles']].dropna()
    elif position == "TE":
        features = nfl_data_position[['receptions', 'receiving_yards', 'receiving_tds', 'receiving_first_downs', 'receiving_fumbles']].dropna()
    
    # Clustering
    kmeans = KMeans(n_clusters=4, random_state=42)
    nfl_data_position['cluster'] = kmeans.fit_predict(features)
    
    # Assigning meaningful labels based on cluster and position
    if position == "QB":
        cluster_labels = {
            0: "Reliably Average",
            1: "Limited Role QB",
            2: "Elite Playmaker",
            3: "Boom or Bust QB"
        }
    elif position == "RB":
        cluster_labels = {
            0: "Consistently Dependable",
            1: "Backup/Rotational", 
            2: "Elite Workhorse", 
            3: "Versatile Contributor" 
        }
    elif position == "WR":
        cluster_labels = {
            0: "Depth Option",
            1: "Go-To Receiver", 
            2: "Role Player",
            3: "Consistent WR2" 
        }
    elif position == "TE":
        cluster_labels = {
            0: "Limited Contributor", 
            1: "Dependable Target", 
            2: "Elite Playmaker",
            3: "Run/Pass Blocker"
        }

    nfl_data_position['cluster_label'] = nfl_data_position['cluster'].map(cluster_labels)
    
    # 3D Cluster Plot using Plotly with increased size
    if features.shape[1] >= 3:
        fig = px.scatter_3d(
            nfl_data_position, 
            x=features.columns[0], 
            y=features.columns[1], 
            z=features.columns[2], 
            color='cluster_label', 
            hover_data=['name'],
            title=f"Clustering for: {position}",
        )

        fig.update_layout(
            width=800,
            height=550,
            margin=dict(l=10, r=10, t=30, b=10),
            title=dict(font=dict(size=20)),
            showlegend=False
            # legend=dict(
            #     font=dict(size=12),
            #     orientation="h", 
            #     yanchor="top",
            #     y=.02,
            #     xanchor="center",
            #     x=.05
            # )   
        )
        st.plotly_chart(fig, use_container_width=True)

    
    # Display the players with their cluster labels
    st.write(f"Players in each cluster for position {position}:")
    st.dataframe(nfl_data_position[['name', 'cluster_label', 'team', 'games'] + features.columns.tolist()])
    
    # # Export cluster stats to CSV
    # cluster_stats = nfl_data_position.groupby('cluster_label')[features.columns].mean().reset_index()
    # cluster_stats['position'] = position
    # csv_filename = f"cluster_stats_{position}.csv"
    # cluster_stats.to_csv(csv_filename, index=False)

# Add Streamlit select box for visualization
position = st.selectbox("Select Position to Cluster:", ["QB", "RB", "WR", "TE"])
cluster_and_visualize(nfl_data, position)
