import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# 加载数据集
data = pd.read_csv('A3dataset.csv')

# 创建GT和GN网络
GT = nx.DiGraph()
GN = nx.DiGraph()

# 直接添加边和权重，不使用中间字典
for (nameOrig, nameDest), transaction in data.groupby(['nameOrig', 'nameDest']):
    GT.add_edge(nameOrig, nameDest, weight=transaction['amount'].sum())
    GN.add_edge(nameOrig, nameDest, weight=len(transaction))


# 修改后的团计算函数
def count_cliques_modified(G, max_k=8):
    # 转换为无向图并简化
    G_undirected = G.to_undirected()
    G_undirected.remove_edges_from(nx.selfloop_edges(G_undirected))

    # 初始化结果数组
    clique_counts = [0] * max_k

    # 对于k=1，就是节点数
    clique_counts[0] = G_undirected.number_of_nodes()

    # 对于k=2，就是边数
    clique_counts[1] = G_undirected.number_of_edges()

    # 对于k>=3，使用find_cliques但限制搜索规模
    try:
        for clique in nx.find_cliques(G_undirected):
            size = len(clique)
            if size <= max_k:
                clique_counts[size - 1] += 1
    except:
        print("Warning: Clique computation terminated early")

    return clique_counts


# 计算实际网络中的团数量
gt_cliques = count_cliques_modified(GT)

# 创建较小的ER随机网络进行比较
n = min(1000, GT.number_of_nodes())  # 限制节点数
p = nx.density(GT.to_undirected())
er_graph = nx.erdos_renyi_graph(n, p)
er_cliques = count_cliques_modified(er_graph)

# 绘制Figure 9
plt.figure(figsize=(10, 6))
plt.plot(range(1, 9), gt_cliques, 'ro-', label='Empirical count')
plt.plot(range(1, 9), er_cliques, 'bo-', label='ER expectation')
plt.yscale('log')
plt.xlabel('Clique order (k)')
plt.ylabel('Number of cliques')
plt.title('Number of Cliques in GT Network vs ER Network')
plt.legend()
plt.grid(True)
plt.savefig('Figure_9_Cliques_Distribution.png')
plt.close()
