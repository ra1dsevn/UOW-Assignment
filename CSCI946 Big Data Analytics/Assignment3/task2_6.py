
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import random

# Load the dataset
data = pd.read_csv('A3dataset.csv')

# Create the GT and GN networks
GT = nx.DiGraph()
GN = nx.DiGraph()

# Add edges and weights to the GT network
for (nameOrig, nameDest), transaction in data.groupby(['nameOrig', 'nameDest']):
    weight = transaction['amount'].sum()
    GT.add_edge(nameOrig, nameDest, weight=weight)

# Add edges and weights to the GN network
for (nameOrig, nameDest), transaction in data.groupby(['nameOrig', 'nameDest']):
    weight = len(transaction)
    GN.add_edge(nameOrig, nameDest, weight=weight)

# Get all edges and their weights from both networks
edges_GT = list(GT.edges())
edges_GN = list(GN.edges())

# Ensure we have common edges between networks
common_edges = list(set(edges_GT) & set(edges_GN))

# Randomly sample 10000 edges (or all if less than 10000)
sample_size = min(10000, len(common_edges))
sampled_edges = random.sample(common_edges, sample_size)

# Get weights for sampled edges
weights_GT = [GT[u][v]['weight'] for u, v in sampled_edges]
weights_GN = [GN[u][v]['weight'] for u, v in sampled_edges]

# Calculate Spearman correlation
correlation, p_value = stats.spearmanr(weights_GT, weights_GN)

# Create scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(weights_GT, weights_GN, alpha=0.5)
plt.xscale('log')
plt.yscale('log')

# Add title and labels
plt.title(f'Edge Weight Correlation\nSpearman Correlation: {correlation:.2f}')
plt.xlabel('GT Network Edge Weights (Total Amount)')
plt.ylabel('GN Network Edge Weights (Number of Transactions)')

# Add grid
plt.grid(True, which="both", ls="--", alpha=0.3)

# Add text box with correlation coefficient
plt.text(0.05, 0.95, f'ρ = {correlation:.2f}',
         transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.8))

# Save the figure
plt.savefig('Figure_6_Edge_Weight_Correlation.png', dpi=300, bbox_inches='tight')
plt.show()
