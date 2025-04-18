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

# Calculate in-strength and out-strength for both networks
def get_strength_distributions(G):
    in_strength = dict(G.in_degree(weight='weight'))
    out_strength = dict(G.out_degree(weight='weight'))
    return list(in_strength.values()), list(out_strength.values())

# Get strength distributions
in_strength_GT, out_strength_GT = get_strength_distributions(GT)
in_strength_GN, out_strength_GN = get_strength_distributions(GN)

# Calculate cumulative distributions
def cumulative_distribution(values):
    sorted_values = np.sort(values)
    cum_prob = 1 - np.linspace(0, 1, len(sorted_values))
    return sorted_values, cum_prob

# Calculate cumulative distributions for all strength values
in_sorted_GT, in_cum_GT = cumulative_distribution(in_strength_GT)
out_sorted_GT, out_cum_GT = cumulative_distribution(out_strength_GT)
in_sorted_GN, in_cum_GN = cumulative_distribution(in_strength_GN)
out_sorted_GN, out_cum_GN = cumulative_distribution(out_strength_GN)

# Create the plot
plt.figure(figsize=(12, 6))

# Plot GT distributions
plt.subplot(121)
plt.loglog(in_sorted_GT, in_cum_GT, 'r-', label='In-strength')
plt.loglog(out_sorted_GT, out_cum_GT, 'b-', label='Out-strength')
plt.title('GT Network')
plt.xlabel('Strength')
plt.ylabel('P(X ≥ x)')
plt.legend()
plt.grid(True, which="both", ls="--")

# Plot GN distributions
plt.subplot(122)
plt.loglog(in_sorted_GN, in_cum_GN, 'r-', label='In-strength')
plt.loglog(out_sorted_GN, out_cum_GN, 'b-', label='Out-strength')
plt.title('GN Network')
plt.xlabel('Strength')
plt.ylabel('P(X ≥ x)')
plt.legend()
plt.grid(True, which="both", ls="--")

plt.suptitle('Cumulative In-strength and Out-strength Distribution')
plt.tight_layout()

# Save the figure
plt.savefig('Figure_7_Cumulative_In_Out_Strength_Distribution.png', dpi=300, bbox_inches='tight')
plt.show()
