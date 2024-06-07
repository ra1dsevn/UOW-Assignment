import numpy as np

# Define a 5x5 proximity matrix with some example values
proximity_matrix = np.array([
    [0, 2, 3, 4, 5], # C1
    [2, 0, 6, 7, 8], # C2
    [3, 6, 0, 1, 3], # C3
    [4, 7, 1, 0, 2], # C4
    [5, 8, 3, 2, 0]  # C5
])

# Function to merge two clusters
def merge_clusters(matrix, cluster_index1, cluster_index2):
    # Choose the minimum distance as the distance of the new cluster to other clusters
    new_distances = np.minimum(matrix[cluster_index1, :], matrix[cluster_index2, :])
    # Remove the old rows and columns
    matrix = np.delete(matrix, [cluster_index1, cluster_index2], axis=0)
    matrix = np.delete(matrix, [cluster_index1, cluster_index2], axis=1)
    # Add the new distances as a new last row and column
    matrix = np.vstack((matrix, new_distances[:-2])) # Exclude the last two distances which are to the old clusters
    matrix = np.column_stack((matrix, np.append(new_distances[:-2], 0))) # Add 0 as the distance to itself
    return matrix

print(proximity_matrix)
print("")
# Merge clusters C3 (index 2) and C4 (index 3) and update the matrix
updated_proximity_matrix = merge_clusters(proximity_matrix, 2, 3)
print(updated_proximity_matrix)
