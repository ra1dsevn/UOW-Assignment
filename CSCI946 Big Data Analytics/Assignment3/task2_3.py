import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset and create network
data = pd.read_csv('A3dataset.csv')
G = nx.DiGraph()
for (nameOrig, nameDest), transaction in data.groupby(['nameOrig', 'nameDest']):
    weight = transaction['amount'].sum()
    G.add_edge(nameOrig, nameDest, weight=weight)

# Get WLCC
wlcc = max(nx.weakly_connected_components(G), key=len)
G_wlcc = G.subgraph(wlcc)

# Calculate degree distributions
in_degrees = [d for n, d in G_wlcc.in_degree()]
out_degrees = [d for n, d in G_wlcc.out_degree()]

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# 绘制入度分布直方图
ax1.hist(in_degrees, bins=20, alpha=0.7, color='blue')
ax1.set_title('In-degree Distribution')
ax1.set_xlabel('In-degree')
ax1.set_ylabel('Frequency')

# 绘制出度分布直方图
ax2.hist(out_degrees, bins=20, alpha=0.7, color='red')
ax2.set_title('Out-degree Distribution')
ax2.set_xlabel('Out-degree')
ax2.set_ylabel('Frequency')

plt.tight_layout()

# 添加统计信息文本框
stats_text = f"""Network Statistics:
Nodes in WLCC: {len(G_wlcc)}
Max in-degree: {max(in_degrees)}
Max out-degree: {max(out_degrees)}
Mean in-degree: {np.mean(in_degrees):.2f}
Mean out-degree: {np.mean(out_degrees):.2f}"""

plt.figtext(0.02, 0.02, stats_text, fontsize=10,
            bbox=dict(facecolor='white', alpha=0.8))

# 保存图表
plt.savefig('Figure_3_Degree_Distributions.png', dpi=300, bbox_inches='tight')
plt.show()

# 打印详细的网络分析
print("\nDetailed Network Analysis:")
print(f"Number of nodes in WLCC: {len(G_wlcc)}")
print(f"Number of edges in WLCC: {G_wlcc.number_of_edges()}")
print("\nDegree Statistics:")
print(f"In-degree distribution: {np.unique(in_degrees, return_counts=True)}")
print(f"Out-degree distribution: {np.unique(out_degrees, return_counts=True)}")

# 找到中心节点
center_node = [n for n, d in G_wlcc.in_degree() if d == max(in_degrees)][0]
print(f"\nCenter node (highest in-degree): {center_node}")
