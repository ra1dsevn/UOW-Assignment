import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 加载数据集
data = pd.read_csv('A3dataset.csv')

# 创建GT和GN网络
GT = nx.DiGraph()
GN = nx.DiGraph()

# 为GT网络添加边和权重
for (nameOrig, nameDest), transaction in data.groupby(['nameOrig', 'nameDest']):
    weight = transaction['amount'].sum()
    GT.add_edge(nameOrig, nameDest, weight=weight)

# 为GN网络添加边和权重
for (nameOrig, nameDest), transaction in data.groupby(['nameOrig', 'nameDest']):
    weight = len(transaction)
    GN.add_edge(nameOrig, nameDest, weight=weight)


# 计算入度和出度强度
def get_strength_data(G):
    in_strength = dict(G.in_degree(weight='weight'))
    out_strength = dict(G.out_degree(weight='weight'))

    # 获取所有节点的入度和出度强度
    nodes = list(G.nodes())
    in_values = [in_strength[node] for node in nodes]
    out_values = [out_strength[node] for node in nodes]

    # 计算Spearman相关系数
    correlation, _ = stats.spearmanr(in_values, out_values)

    return in_values, out_values, correlation


# 获取GT和GN网络的强度数据
gt_in, gt_out, gt_corr = get_strength_data(GT)
gn_in, gn_out, gn_corr = get_strength_data(GN)

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制GT网络数据点（红色）
plt.scatter(gt_in, gt_out, c='red', alpha=0.5, label=f'GT (ρ = {gt_corr:.2f})')

# 绘制GN网络数据点（蓝色）
plt.scatter(gn_in, gn_out, c='blue', alpha=0.5, label=f'GN (ρ = {gn_corr:.2f})')

# 设置坐标轴为对数刻度
plt.xscale('log')
plt.yscale('log')

# 添加标签和标题
plt.xlabel('In-strength')
plt.ylabel('Out-strength')
plt.title('Out-strength versus In-strength for GT and GN Networks')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.3)

# 保存图像
plt.savefig('Figure_8_Out_vs_In_Strength.png', dpi=300, bbox_inches='tight')
plt.close()
