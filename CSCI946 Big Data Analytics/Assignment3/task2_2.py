import random
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the dataset
df = pd.read_csv('A3dataset.csv')

def snowball_sampling_with_levels(graph, initial_node, depth=3):
    sampled_nodes = {initial_node: 0}  # Set the level of the initial node to 0
    nodes_to_explore = set([initial_node])

    for current_depth in range(depth):
        current_nodes = nodes_to_explore
        nodes_to_explore = set()

        for node in current_nodes:
            neighbors = set(graph.neighbors(node))
            for new_node in neighbors:
                if new_node not in sampled_nodes:
                    nodes_to_explore.add(new_node)
                    sampled_nodes[new_node] = current_depth + 1  # Record the level of the node

    return sampled_nodes

# Create the graph
G = nx.from_pandas_edgelist(df, source='nameOrig', target='nameDest')

# Analyze the graph
results = {}
num_samples = 5  # Repeat the sampling 5 times

for _ in range(num_samples):
    # Randomly select 0.1% of the data
    sample_size = int(0.001 * len(G.nodes))
    initial_nodes = random.sample(list(G.nodes), sample_size)

    distance_connections = {i: 0 for i in range(1, 4)}  # Number of connections at distances 1, 2, and 3

    for initial_node in initial_nodes:
        sampled_nodes_with_levels = snowball_sampling_with_levels(G, initial_node, depth=3)
        for level in range(1, 4):
            # Include nodes at level 2 in the count for level 3 as well
            distance_connections[level] += sum(1 for node_level in sampled_nodes_with_levels.values() if node_level <= level)

    for level in range(1, 4):
        distance_connections[level] /= sample_size

    results[_] = distance_connections

# Calculate the average
average_results = {}
for level in range(1, 4):
    average_results[level] = np.mean([result[level] for result in results.values()])

# Plot the graph
plt.figure(figsize=(10, 6))

for i in range(num_samples):
    distances = list(results[i].keys())
    connections = list(results[i].values())
    plt.plot(distances, connections)

# Plot the average line (black dashed line)
average_distances = list(average_results.keys())
average_connections = list(average_results.values())
plt.plot(average_distances, average_connections, '--k')

plt.xlabel('Distance')
plt.ylabel('Ns(l)')
plt.legend()

# Store the title in a variable
title = 'Average Number of nodes (Ns(l)) at distance l'
plt.title(title)

# Replace spaces with underscores and save the figure before showing it
filename = title.replace(' ', '_') + '.png'
plt.savefig(filename)

plt.show()
