import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
data = pd.read_csv('A3dataset.csv')

# Create the directed graph
G = nx.DiGraph()

# Add edges with weights (total transaction amounts) to the graph
for (nameOrig, nameDest), transaction in data.groupby(['nameOrig', 'nameDest']):
    weight = transaction['amount'].sum()
    G.add_edge(nameOrig, nameDest, weight=weight)

# Get the largest weakly connected component (WLCC)
wlcc = max(nx.weakly_connected_components(G), key=len)
G_wlcc = G.subgraph(wlcc).copy()

# Calculate clustering coefficient for nodes in WLCC
clustering_coeffs = nx.clustering(G_wlcc).values()

# Plot clustering coefficient distribution
plt.figure(figsize=(10, 6))
plt.hist(clustering_coeffs, bins=np.logspace(np.log10(0.001), np.log10(1), 50), color='skyblue', alpha=0.7)
plt.xscale('log')
plt.xlabel('Clustering Coefficient')
plt.ylabel('Frequency')
plt.title('Distribution of Clustering Coefficient in WLCC')
plt.grid(True, which='both', ls='--', lw=0.5)

# Save and show plot
plt.savefig('Figure_10_Clustering_Coefficient_Distribution.png', dpi=300, bbox_inches='tight')
plt.show()
