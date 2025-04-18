# Install and load the necessary libraries
library(caret)
library(pROC)
library(gplots)

# Read twitter_data
setwd("/Users/liyinqiao/Downloads/Assignmeng2")
twitter_data <- read.csv("twitter_user_data.csv")
twitter_data <- na.omit(twitter_data)

# Explore data
head(twitter_data)
summary(twitter_data)

# Divide the Training and Test sets
set.seed(123)
trainIndex <- sample(1:nrow(twitter_data), 0.7*nrow(twitter_data))
trainData <- twitter_data[trainIndex,]
testData <- twitter_data[-trainIndex,]
trainData$retweet_count <- ifelse(trainData$retweet_count > 0.5, 1, 0)
testData$retweet_count <- ifelse(testData$retweet_count > 0.5, 1, 0)

# Train Logistic Regression
logistic_model <- glm(retweet_count ~ fav_number, data = trainData, family = "binomial")

# Prediction
logistic_predictions <- predict(logistic_model, newdata = testData, type = "response")
logistic_predictions <- ifelse(logistic_predictions > 0.5, 1, 0)

# Visualization
plot(logistic_model, method = "scatterplot")