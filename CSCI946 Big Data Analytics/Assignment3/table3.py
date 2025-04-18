import pandas as pd
import networkx as nx
import numpy as np
from collections import Counter
from math import comb
import matplotlib.pyplot as plt
import seaborn as sns


def er_clique_expectation(n, p, k):
    """
    计算Erdős-Rényi随机图中k阶团的期望数量

    参数:
    n: 节点数量
    p: 边概率
    k: 团的阶数

    返回:
    float: k阶团的期望数量
    """
    if k == 1:
        return n
    elif k == 2:
        return int(n * (n - 1) * p / 2)
    else:
        # 对于k>2的情况，使用组合数和边概率计算
        expected = comb(n, k) * (p ** (k * (k - 1) / 2))
        return expected


def improved_clique_count(G, max_k=8):
    # 保持原有的团计数功能
    G_undirected = G.to_undirected()
    G_undirected.remove_edges_from(nx.selfloop_edges(G_undirected))
    results = np.zeros(max_k, dtype=int)
    results[0] = G_undirected.number_of_nodes()
    results[1] = G_undirected.number_of_edges()
    cliques = list(nx.find_cliques(G_undirected))
    clique_sizes = Counter(len(c) for c in cliques)
    for size, count in clique_sizes.items():
        if 2 < size <= max_k:
            results[size - 1] = count
    return results


def visualize_degree_distribution(G):
    in_degrees = [d for n, d in G.in_degree()]
    out_degrees = [d for n, d in G.out_degree()]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    # 入度分布
    sns.histplot(in_degrees, ax=ax1, bins=50)
    ax1.set_title('In-degree Distribution')
    ax1.set_xlabel('In-degree')
    ax1.set_ylabel('Count')
    ax1.set_yscale('log')

    # 出度分布
    sns.histplot(out_degrees, ax=ax2, bins=50)
    ax2.set_title('Out-degree Distribution')
    ax2.set_xlabel('Out-degree')
    ax2.set_ylabel('Count')
    ax2.set_yscale('log')

    plt.tight_layout()
    plt.savefig('degree_distribution.png')
    plt.close()


def analyze_network(data_path):
    # 读取数据和基本分析
    data = pd.read_csv(data_path)
    edges = data.groupby(['nameOrig', 'nameDest'])['amount'].sum().reset_index()
    GT = nx.from_pandas_edgelist(edges, 'nameOrig', 'nameDest', 'amount', create_using=nx.DiGraph())

    # 计算团和ER期望值
    gt_cliques = improved_clique_count(GT)
    n = GT.number_of_nodes()
    p = nx.density(GT.to_undirected())
    er_expectations = [er_clique_expectation(n, p, k) for k in range(1, 9)]

    # 创建结果表格
    df = pd.DataFrame({
        'Clique Order (k)': range(1, 9),
        'Empirical Count': gt_cliques,
        'ER Expectation': er_expectations
    })
    df.set_index('Clique Order (k)', inplace=True)
    df = df.map(lambda x: '{:.2e}'.format(x))

    # 打印基本结果
    print("\nFigure 9: Number of cliques in Rabobank network")
    print("=" * 50)
    print(df.to_string())
    df.to_csv('Figure_9_Cliques_Table.csv')

    # 扩展网络分析
    print("\nAdditional Network Analysis:")
    print("=" * 50)
    print(f"Number of nodes: {GT.number_of_nodes()}")
    print(f"Number of edges: {GT.number_of_edges()}")
    print(f"Network density: {nx.density(GT):.6f}")
    print(f"Is connected: {nx.is_strongly_connected(GT)}")

    # 度分析
    in_degrees = [d for n, d in GT.in_degree()]
    out_degrees = [d for n, d in GT.out_degree()]
    print(f"Average in-degree: {np.mean(in_degrees):.2f}")
    print(f"Average out-degree: {np.mean(out_degrees):.2f}")
    print(f"Max in-degree: {max(in_degrees)}")
    print(f"Max out-degree: {max(out_degrees)}")

    # 添加连通分量分析
    weakly_connected = nx.number_weakly_connected_components(GT)
    print(f"\nNumber of weakly connected components: {weakly_connected}")

    # 可视化度分布
    visualize_degree_distribution(GT)


if __name__ == "__main__":
    analyze_network('A3dataset.csv')
