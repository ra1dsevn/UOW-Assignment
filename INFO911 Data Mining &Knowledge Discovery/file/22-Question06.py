import math

# Function to calculate entropy for a node
def calculate_entropy(class_counts):
    total_count = sum(class_counts)
    entropy = sum([(count / total_count) * math.log2(total_count / count) for count in class_counts if count > 0])
    return entropy

# Calculate entropy for the root node
root_counts = [10, 10, 10]
root_entropy = calculate_entropy(root_counts)

# Calculate entropy for the left node
left_counts = [4, 3, 4]
left_entropy = calculate_entropy(left_counts)

# Calculate entropy for the right node
right_counts = [6, 7, 6]
right_entropy = calculate_entropy(right_counts)

# Calculate the weighted entropy after the split (total_count = 30 for the root node)
weighted_entropy = (sum(left_counts)/sum(root_counts)) * left_entropy + (sum(right_counts)/sum(root_counts)) * right_entropy

# Calculate the entropy gain from the root node to the split
entropy_gain = root_entropy - weighted_entropy

# Print out the entropy gain
print(f'Root Entropy: {root_entropy}')
print(f'Left Entropy: {left_entropy}')
print(f'Right Entropy: {right_entropy}')
print(f'Weighted Entropy: {weighted_entropy}')
print(f'Entropy Gain: {entropy_gain}')