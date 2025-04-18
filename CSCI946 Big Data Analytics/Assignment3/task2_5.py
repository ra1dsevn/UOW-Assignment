import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

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

# Calculate cumulative distribution
def cumulative_distribution(weights):
    sorted_weights = np.sort(weights)
    # Using 1 - P to show the probability of weights greater than x
    cum_prob = 1 - np.linspace(0, 1, len(sorted_weights))
    return sorted_weights, cum_prob

# Get weights from networks
weights_GT = [d['weight'] for (u, v, d) in GT.edges(data=True)]
weights_GN = [d['weight'] for (u, v, d) in GN.edges(data=True)]

# Calculate cumulative distributions
sorted_weights_GT, cum_prob_GT = cumulative_distribution(weights_GT)
sorted_weights_GN, cum_prob_GN = cumulative_distribution(weights_GN)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot both distributions
plt.loglog(sorted_weights_GT, cum_prob_GT, 'r-', label='GT (Transaction Amount)', linewidth=2)
plt.loglog(sorted_weights_GN, cum_prob_GN, 'b-', label='GN (Transaction Count)', linewidth=2)

# Customize the plot
plt.title('Cumulative Edge-weight Distribution')
plt.xlabel('Edge Weight (w)')
plt.ylabel('P(W ≥ w)')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.3)

# Add text box with distribution information
gt_max = np.max(weights_GT)
gn_max = np.max(weights_GN)
plt.text(0.05, 0.95, f'GT max: {gt_max:.2f}\nGN max: {gn_max:.2f}',
         transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.8))

# Save the figure
plt.savefig('Figure_5_Cumulative_Edge_Weight_Distribution.png', dpi=300, bbox_inches='tight')
plt.show()
