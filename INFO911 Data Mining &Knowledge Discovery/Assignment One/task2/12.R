# 设定SOM网络结构
som_grid <- somgrid(xdim = 7, ydim=7, topo="hexagonal")

# 将PCA转换后的特征作为SOM模型的输入
# 移除目标变量 credit.rating
data_train_pca_som <- data_train_pca[, -ncol(data_train_pca)]

# 训练SOM模型
system.time(som_model <- som(data_train_pca_som, grid=som_grid,
                             rlen=1000, alpha=c(0.5, 0.05), keep.data = TRUE))

# 可视化SOM模型的不同属性
source('./coolBlueHotRed.R')  # 确保你有这个文件和函数，用于定义颜色

# 变化图
plot(som_model, type = "changes", main="SOM training changes", palette.name=coolBlueHotRed)

# 节点计数图
plot(som_model, type = "counts", main="Node Counts", palette.name=coolBlueHotRed)

# 映射质量图
plot(som_model, type = "quality", main="Node Quality/Distance", palette.name=coolBlueHotRed)

# 邻居距离图
plot(som_model, type="dist.neighbours", main = "SOM neighbour distances", palette.name=grey.colors)

# 使用主成分1的值绘制属性热图
var <- 1  # 这里假设我们关注第一个主成分
plot(som_model, type = "property", property = som_model$codes[[1]][,var], main=paste("Component", var, "Heatmap"), palette.name=coolBlueHotRed)

# 下面的K-means聚类可以保持不变，但请注意，聚类是在SOM代码向量的基础上进行的

# 下面的代码对SOM模型结果进行聚类分析
# 使用K-means聚类并展示WCSS图以便判断聚类数量
mydata <- som_model$codes[[1]]  # 使用SOM模型的代码簿作为聚类的输入数据
wss <- (nrow(mydata) - 1) * sum(apply(mydata, 2, var))

# 继续之前的SOM分析和聚类
# 显示SOM的代码簿
plot(som_model, type = "codes")

# 使用K-means聚类并展示WCSS图以便判断聚类数量
mydata <- som_model$codes[[1]]  # 使用SOM模型的代码簿作为聚类的输入数据
wss <- (nrow(mydata) - 1) * sum(apply(mydata, 2, var))

for (i in 2:15) {
  set.seed(123)  # 可以设置种子以便结果的重复性
  wss[i] <- sum(kmeans(mydata, centers=i)$withinss)
}

par(mar=c(5.1, 4.1, 4.1, 2.1))
plot(1:15, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares", main="WCSS for Different Numbers of Clusters")

# 确定最佳聚类数
optimal_clusters <- which.min(wss)
cat("The optimal number of clusters is", optimal_clusters, "\n")

# 对SOM代码簿向量应用最佳数量的聚类
set.seed(123) # 为了可重复性
kmeans_result <- kmeans(mydata, centers=optimal_clusters)

# 在SOM映射上显示聚类结果
plot(som_model, type="mapping", bgcol=pretty_palette[kmeans_result$cluster], main="Cluster Mapping")
add.cluster.boundaries(som_model, kmeans_result$cluster)

# 打印完整的K-means聚类结果
print(kmeans_result)