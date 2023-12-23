import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

## assigning csv to dataframe
nhl_data_original = pd.read_csv('/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/CSVs/NHL_2022_2023_skaters.csv')
## filtering for 5 on 5 situations only
nhl_data_original = nhl_data_original[nhl_data_original['situation']=='5on5']

nhl_data = nhl_data_original

## selecting columns I want to use for my model and assigning to nhl_data variable
selected_columns = [
    'playerId',
    'I_F_goals', 
    'I_F_primaryAssists', 
    'I_F_points',
    'I_F_shotsOnGoal', 
    'faceoffsWon',
    'penalityMinutes',
    'I_F_hits',
    'I_F_takeaways',
    'I_F_giveaways']
nhl_data = nhl_data[selected_columns]

X = nhl_data.drop('playerId', axis=1)  # Exclude playerId for clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA 
pca = PCA()
pca.fit(X_scaled)

## PCA stats
component_stats = pd.DataFrame({
    'Component': range(1, pca.n_components_ + 1),
    'Explained Variance Ratio': pca.explained_variance_ratio_,
    'Cumulative Explained Variance': pca.explained_variance_ratio_.cumsum()
})

## pushing PCA stats to a csv
component_stats.to_csv('/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/CSVs/NHL_pca_stats.csv', index=False)

#--------------------------Uncomment if you want to plot PCA---------------------------------------------------
## plotting PCA results
# # Plotting the explained variance ratio to help choose the number of components
# plt.plot(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_.cumsum(), marker='o')
# plt.xlabel('Number of Components')
# plt.ylabel('Cumulative Explained Variance')
# plt.show()

## assigning components
optimal_components = 2
pca = PCA(n_components=optimal_components)
X_pca = pca.fit_transform(X_scaled)

#--------------------------Uncomment if you want print loadings---------------------------------------------------
# # Print the DataFrame
# # Create a DataFrame with loadings for the selected components
# loadings_df = pd.DataFrame(pca.components_[:optimal_components].T, columns=[f'PC{i+1}' for i in range(optimal_components)], index=X.columns)
# print(loadings_df)

#--------------------------Uncomment if you want elbow method for optimal K---------------------------------------------------
## elbow method for optimal K
# inertia = []
# for k in range (1,8): ## update thise depending on number of features
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     kmeans.fit(X_pca)
#     inertia.append(kmeans.inertia_)

# ## plotting elbow results
# plt.plot(range(1, 8), inertia, marker='o') ## update thise depending on number of features
# plt.xlabel('Number of Clusters (K)')
# plt.ylabel('Inertia')
# plt.show()

# Extract PC1 and PC2 from the PCA-transformed data
nhl_data['PC1'] = X_pca[:, 0]
nhl_data['PC2'] = X_pca[:, 1]

#--------------------------Uncomment if you want silhouette method for optimal K---------------------------------------------------
# # Determine optimal K using silhouette score
max_k = 10  # Set the maximum number of clusters to consider
best_score = float('-inf')  # Initialize with negative infinity to ensure any valid score is an improvement
best_k = 0

for k in range(2, max_k + 1):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    
#     print(f"For K={k}, silhouette score: {score}")

optimal_k = 4

## KMeans clustering
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
nhl_data['cluster'] = kmeans.fit_predict(X_pca)

cluster_stats = nhl_data.drop('playerId', axis=1).groupby('cluster').mean()
cluster_stats = cluster_stats.round(2)

cluster_stats.to_csv('/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/CSVs/NHL_cluster_results.csv')


# for cluster_id in nhl_data['cluster'].unique():
#     cluster_data = nhl_data[nhl_data['cluster'] == cluster_id]
#     plt.scatter(cluster_data['PC1'], cluster_data['PC2'], label=f'Cluster {cluster_id}')

# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.title('Clusters in 2D Space (PC1 vs PC2)')

# plt.legend()
# plt.show()

nhl_data_labeled = nhl_data.copy()  # Create a copy of the original DataFrame

# Initialize the new column with a default label
nhl_data_labeled['cluster_label'] = 'Unknown'

# Assign labels based on cluster
nhl_data_labeled.loc[nhl_data_labeled['cluster'] == 0, 'cluster_label'] = 'Bruiser'
nhl_data_labeled.loc[nhl_data_labeled['cluster'] == 1, 'cluster_label'] = 'Defensive Minded'
nhl_data_labeled.loc[nhl_data_labeled['cluster'] == 2, 'cluster_label'] = 'Offensive All Star'
nhl_data_labeled.loc[nhl_data_labeled['cluster'] == 3, 'cluster_label'] = 'Support Player'

nhl_data_labeled.to_csv('/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/CSVs/nhl_data_labeled.csv', index=False)

nhl_player_cluster_final = pd.merge(nhl_data_labeled, nhl_data_original[['playerId', 'name', 'team']], on='playerId', how='left')

selected_features = [
    'name',
    'team',
    'cluster_label']

nhl_player_cluster_final = nhl_player_cluster_final[selected_features]
nhl_player_cluster_final.to_csv('/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/CSVs/nhl_cluster_final.csv', index=False)
