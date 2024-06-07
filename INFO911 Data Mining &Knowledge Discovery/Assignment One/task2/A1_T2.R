library(class)
library(MASS)
library(Hmisc)
library(kohonen)
library(dummy)
library(ggplot2)
library(sp)
library(tmaptools)
library(reshape2)
library(geos)
library(caret) #用于PCA
library(corrplot) # 可视化库
library(rpart) # 决策树包

#设定工作目录及数据加载
setwd("D:/lyq/Ass2")
pretty_palette <- c("#1f77b4", '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2')
data_raw <- read.csv("./creditworthiness.csv")
# 筛选出有效数据，这里credit.rating=0即为无效数据
sub_index_1 = which(data_raw$credit.rating != 0)
# 计算筛选后的数量，随机分配训练集和测试集
sub_group_num = NROW(sub_index_1)
rand_idx = sample(x=1:sub_group_num, size=sub_group_num*0.9, replace=FALSE)
data_train_idx=sub_index_1[rand_idx]
data_test_idx=sub_index_1[-rand_idx]
# 创建训练集 测试集
data_train=data_raw[data_train_idx,]
data_test=data_raw[data_test_idx,]
data_verify=data_raw[-sub_index_1,]

############################################PCA分析############################################
# 在执行PCA之前，对数据进行准备，这里不包括目标变量credit.rating
numeric_columns_indices <- which(sapply(data_raw, is.numeric) & names(data_raw) != "credit.rating")
numerical_columns <- data_raw[, numeric_columns_indices]

# 执行PCA分析
pca_result <- prcomp(numerical_columns, center = TRUE, scale. = TRUE)

# 获取主成分分析（PCA）的结果
explained_variance <- pca_result$sdev ^ 2
total_variance <- sum(explained_variance)
explained_variance_ratio <- explained_variance / total_variance
weighted_contributions <- abs(pca_result$rotation) %*% explained_variance_ratio
feature_importance <- apply(weighted_contributions, 1, sum)

# 使用numeric_columns_indices中的索引来标记特征名称
names(feature_importance) <- names(numerical_columns)

# 根据特征的重要性创建数据框，准备输出至CSV文件
output_df <- data.frame(FeatureNo = numeric_columns_indices,
                        Feature = names(feature_importance), 
                        Importance = feature_importance)

# 按特征重要性对数据框进行排序
output_df <- output_df[order(-output_df$Importance), ]

# 输出至CSV文件
write.csv(output_df, 'PCA_Features_Importance_with_Original_Column_No.csv', row.names = FALSE)
############################################PCA分析结束############################################
############################################利用PCA结果来作为训练的特征############################################
data_train_extract=data_train[,c(34,29,9,13,23)]
data_train_matrix <- as.matrix(scale(data_train_extract))
names(data_train_matrix) <- names(data_train_extract)
require(kohonen)
som_grid <- somgrid(xdim = 7, ydim=7, topo="hexagonal")  
system.time(som_model <- som(data_train_matrix, 
                             grid=som_grid, 
                             rlen=10000, 
                             alpha=c(0.5,0.1), 
                             keep.data = TRUE ))

######################################################################
source('./coolBlueHotRed.R')

# Define alpha and create a string to be appended to filenames
alpha_values <- (0.5,0.1)  # Adjust these values based on your alpha parameter
alpha_str <- paste(alpha_values, collapse = "_")  

# Saving the changes plot to current working directory
png(filename = sprintf("SOM_changes_plot_alpha%s.png", alpha_str))
plot(som_model, type = "changes")
dev.off() # Close the imaging device

# Saving the counts within nodes plot
png(filename = sprintf("SOM_counts_plot_alpha%s.png", alpha_str))
plot(som_model, type = "counts", main="Node Counts", palette.name=coolBlueHotRed)
dev.off() # Close the imaging device

# Saving the map quality plot
png(filename = sprintf("SOM_quality_plot_alpha%s.png", alpha_str))
plot(som_model, type = "quality", main="Node Quality/Distance", palette.name=coolBlueHotRed)
dev.off() # Close the imaging device

# Saving the neighbour distances plot
png(filename = sprintf("SOM_dist_neighbours_plot_alpha%s.png", alpha_str))
plot(som_model, type="dist.neighbours", main = "SOM neighbour distances", palette.name=grey.colors)
dev.off() # Close the imaging device

# Saving the code spread plot
png(filename = sprintf("SOM_code_spread_plot_alpha%s.png", alpha_str))
plot(som_model, type = "codes")
dev.off() # Close the imaging device

# Saving the heatmap for a variable at scaled / normalised values
png(filename = sprintf("SOM_heatmap_var1_alpha%s.png", alpha_str))
var <- 1
plot(som_model, type = "property", property = som_model$codes[[1]][,var], main=names(som_model$data[[1]])[var], palette.name=coolBlueHotRed)
dev.off() # Close the imaging device

# Saving the original scale heatmap for a variable from the training set
png(filename = sprintf("SOM_original_scale_heatmap_var6_alpha%s.png", alpha_str))
var <- 6
var_unscaled <- aggregate(as.numeric(data_train[,var]), by=list(som_model$unit.classif), FUN=mean, simplify=TRUE)[,2]
plot(som_model, type = "property", property=var_unscaled, main=names(data_train)[var], palette.name=coolBlueHotRed)
dev.off() # Close the imaging device
rm(var_unscaled, var)

# Saving the WCSS plot
png(filename = sprintf("SOM_WCSS_plot_alpha%s.png", alpha_str))
plot(1:15, wss, type="b", xlab="Number of Clusters", ylab="Within groups sum of squares", main="Within cluster sum of squares (WCSS)")
dev.off() # Close the imaging device

# Saving the cluster mapping plot
png(filename = sprintf("SOM_cluster_mapping_plot_alpha%s.png", alpha_str))
plot(som_model, type="mapping", bgcol = pretty_palette[som_cluster], main = "Clusters")
add.cluster.boundaries(som_model, som_cluster)
dev.off() # Close the imaging device

# Saving the cluster codes plot
png(filename = sprintf("SOM_cluster_codes_plot_alpha%s.png", alpha_str))
plot(som_model, type="codes", bgcol = pretty_palette[som_cluster], main = "Clusters")
add.cluster.boundaries(som_model, som_cluster)
dev.off() # Close the imaging device
######################################################################








































######################################################################
source('./coolBlueHotRed.R')

plot(som_model, type = "changes")
#counts within nodes
plot(som_model, type = "counts", main="Node Counts", palette.name=coolBlueHotRed)
#map quality
plot(som_model, type = "quality", main="Node Quality/Distance", palette.name=coolBlueHotRed)
#neighbour distances
plot(som_model, type="dist.neighbours", main = "SOM neighbour distances", palette.name=grey.colors)
#code spread
plot(som_model, type = "codes")

# Plot the heatmap for a variable at scaled / normalised values
var <- 1
plot(som_model, type = "property", property = som_model$codes[[1]][,var], main=names(som_model$data[[1]])[var], palette.name=coolBlueHotRed)

# Plot the original scale heatmap for a variable from the training set:
var <- 6#define the variable to plot
var_unscaled <- aggregate(as.numeric(data_train[,var]), by=list(som_model$unit.classif), FUN=mean, simplify=TRUE)[,2]
plot(som_model, type = "property", property=var_unscaled, main=names(data_train)[var], palette.name=coolBlueHotRed)
rm(var_unscaled, var)


# ------------------ Clustering SOM results -------------------

# show the WCSS metric for kmeans for different clustering sizes.
# Can be used as a "rough" indicator of the ideal number of clusters
mydata <- data.frame(som_model$codes)
wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(mydata,
                                     centers=i)$withinss)
par(mar=c(5.1,4.1,4.1,2.1))
plot(1:15, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares", main="Within cluster sum of squares (WCSS)")

# Form clusters on grid
## use hierarchical clustering to cluster the codebook vectors
som_cluster <- cutree(hclust(dist(som_model$codes[[1]])), 5)

# Show the map with different colours for every cluster						  
plot(som_model, type="mapping", bgcol = pretty_palette[som_cluster], main = "Clusters")
add.cluster.boundaries(som_model, som_cluster)

#show the same plot with the codes instead of just colours
plot(som_model, type="codes", bgcol = pretty_palette[som_cluster], main = "Clusters")
add.cluster.boundaries(som_model, som_cluster)



