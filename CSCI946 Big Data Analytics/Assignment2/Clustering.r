# Import the necessary libraries
library(cluster)
library(ggplot2)
library(factoextra)
library(dplyr)

# Read twitter_data
setwd("/Users/liyinqiao/Downloads/Assignmeng2")
twitter_data <- read.csv("twitter_user_data.csv", header=TRUE, sep=",")


# Feature selection for clustering
selected_features <- twitter_data[, c("fav_number", "retweet_count", "tweet_count")]

# Clustering operation, set seeds to ensure repeatability of results
set.seed(123) 
#The K-means algorithm is used for clustering, and it is assumed that the clustering is of 3 categories
kmeans_model <- kmeans(selected_features, centers=3, nstart=25) 

# Visualize the clustering results
fviz_cluster(kmeans_model, data = selected_features,
             geom = "point", stand = FALSE,
             ellipse.type = "t", ellipse.level = 0.6) +
  theme_minimal()


# Output cluster evaluation
silhouette_score <- silhouette(kmeans_model$cluster, dist(selected_features))
fviz_silhouette(silhouette_score)  