import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# 创建示例数据
X = np.array([[1, 2], [2, 3], [3, 4], [3, 1], [4, 2], [5, 3]])
y = np.array([0, 0, 0, 1, 1, 1])  # 0 表示类别1，1 表示类别2

# 初始化LDA模型
lda = LinearDiscriminantAnalysis(n_components=1)

# 拟合数据并进行降维
X_lda = lda.fit_transform(X, y)

# 绘制降维后的数据
plt.figure(figsize=(8, 6))
plt.scatter(X_lda[y == 0], np.zeros(len(X_lda[y == 0])), color='r', label='Class 1')
plt.scatter(X_lda[y == 1], np.zeros(len(X_lda[y == 1])), color='b', label='Class 2')
plt.title('LDA Dimensionality Reduction')
plt.xlabel('LDA Component')
plt.legend()
plt.show()
