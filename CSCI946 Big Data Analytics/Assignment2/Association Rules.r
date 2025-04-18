# Install and load the necessary libraries
library(arules)
library(arulesViz)

# Read twitter_data
setwd("/Users/liyinqiao/Downloads/Assignmeng2")
twitter_data <- read.csv("twitter_user_data.csv")
twitter_data <- na.omit(twitter_data)

# Association Rules
rules <- apriori(twitter_data, parameter = list(support = 0.1, confidence = 0.8))

# Explore data
summary(rules)

# Visualization
plot(rules, method = "scatterplot")

# Method 2 of Visualization, Use jitter = 0 to prevent jitter
plot(rules, method = "scatterplot", jitter = 0)

