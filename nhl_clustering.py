import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

## assigning csv to dataframe
nhl_data = pd.read_csv('/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/CSVs/NHL_2022_2023_skaters.csv')

## filtering for 5 on 5 situations only
nhl_data = nhl_data[nhl_data['situation'] =='5on5']

## selecting columns I want to use for my model and assigning to nhl_data variable
selected_columns = [
    'playerId',
    'I_F_goals', 
    'I_F_primaryAssists', 
    'I_F_secondaryAssists',
    'I_F_points',
    'I_F_shotsOnGoal', 
    'faceoffsWon',
    'penalityMinutes']
nhl_data = nhl_data[selected_columns]

X = nhl_data.drop('playerId', axis=1)  # Exclude playerId for clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Finding optimal PCA components
pca = PCA()
pca.fit(X_scaled)

# Get component stats
component_stats = pd.DataFrame({
    'Component': range(1, pca.n_components_ + 1),
    'Explained Variance Ratio': pca.explained_variance_ratio_,
    'Cumulative Explained Variance': pca.explained_variance_ratio_.cumsum()
})

component_stats.to_csv('/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/CSVs/NHL_pca_stats.csv', index=False)

# # Plotting the explained variance ratio to help choose the number of components
# plt.plot(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_.cumsum(), marker='o')
# plt.xlabel('Number of Components')
# plt.ylabel('Cumulative Explained Variance')
# plt.show()


