import random
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据集
df = pd.read_csv('A3dataset.csv')

# 构建图
G = nx.from_pandas_edgelist(df, source='nameOrig', target='nameDest')

def snowball_sampling_with_levels(graph, initial_node, depth=3):
    """执行 Snowball Sampling，返回节点和其层次信息。"""
    sampled_nodes = {initial_node: 0}  # 初始节点的层次为 0
    nodes_to_explore = set([initial_node])

    for current_depth in range(depth):
        current_nodes = nodes_to_explore
        nodes_to_explore = set()

        for node in current_nodes:
            neighbors = set(graph.neighbors(node))
            for neighbor in neighbors:
                if neighbor not in sampled_nodes:
                    nodes_to_explore.add(neighbor)
                    sampled_nodes[neighbor] = current_depth + 1

    return sampled_nodes

# 随机选择一个源节点
source_node = random.choice(list(G.nodes))

# 执行 Snowball Sampling
sampled_nodes_with_levels = snowball_sampling_with_levels(G, source_node, depth=3)

# 提取采样子图
sampled_nodes = list(sampled_nodes_with_levels.keys())
subgraph = G.subgraph(sampled_nodes)

# 根据总度数设置节点大小和颜色
node_sizes = [100 + 50 * subgraph.degree[node] for node in subgraph]
node_colors = [subgraph.degree[node] for node in subgraph]

# 绘制图
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(subgraph, seed=42)  # 使用 spring_layout 布局节点位置
nodes = nx.draw_networkx_nodes(subgraph, pos, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.viridis)
nx.draw_networkx_edges(subgraph, pos, alpha=0.5)
nx.draw_networkx_labels(subgraph, pos, font_size=8)

# 添加颜色条
ax = plt.gca()  # 获取当前轴
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
sm.set_array([])
plt.colorbar(sm, ax=ax, label='Total Degree')

# 添加标题并显示
plt.title(f"Subgraph Sampled Using Snowball Sampling (l=3, Source Node: {source_node})")
plt.axis("off")
plt.show()
