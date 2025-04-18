import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load the dataset
data = pd.read_csv('A3dataset.csv')

# Create the directed graph (using GT network as base)
G = nx.DiGraph()

# Add edges with weights (total transaction amounts) to the graph
for (nameOrig, nameDest), transaction in data.groupby(['nameOrig', 'nameDest']):
    weight = transaction['amount'].sum()
    G.add_edge(nameOrig, nameDest, weight=weight)

# Get the largest weakly connected component (WLCC)
wlcc = max(nx.weakly_connected_components(G), key=len)
G_wlcc = G.subgraph(wlcc).copy()

# Calculate in-degrees and out-degrees for all nodes in WLCC
in_degrees = dict(G_wlcc.in_degree())
out_degrees = dict(G_wlcc.out_degree())

# Create lists of degrees for nodes that have both in and out degrees
nodes = list(G_wlcc.nodes())
in_deg = [in_degrees[node] for node in nodes]
out_deg = [out_degrees[node] for node in nodes]

# Calculate Spearman correlation
correlation, p_value = stats.spearmanr(in_deg, out_deg)

# Create scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(in_deg, out_deg, alpha=0.5, s=5)
plt.xscale('log')
plt.yscale('log')

# Add title and labels
plt.title('Out-degree vs In-degree in WLCC')
plt.xlabel('In-degree')
plt.ylabel('Out-degree')

# Add grid
plt.grid(True, which="both", ls="--", alpha=0.3)

# Add text box with correlation coefficient
plt.text(0.05, 0.95, f'Spearman ρ = {correlation:.2f}\np-value = {p_value:.2e}',
         transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.8))

# Add diagonal line for reference (y=x)
max_deg = max(max(in_deg), max(out_deg))
min_deg = min(min(in_deg), min(out_deg))
plt.plot([min_deg, max_deg], [min_deg, max_deg], 'r--', alpha=0.5, label='y=x')

plt.legend()

# Show and save the figure
plt.savefig('Figure_4_Degree_Correlation.png', dpi=300, bbox_inches='tight')
plt.show()

# Print additional statistics
print(f"Number of nodes in WLCC: {len(nodes)}")
print(f"Average in-degree: {np.mean(in_deg):.2f}")
print(f"Average out-degree: {np.mean(out_deg):.2f}")
