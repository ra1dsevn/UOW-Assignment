# Install and load the necessary libraries
library(randomForest)
library(ggplot2)

# Read data
setwd("/Users/liyinqiao/Downloads/Assignmeng2")
twitter_data <- read.csv("twitter_user_data.csv")

# Explore data
head(twitter_data)
summary(twitter_data)
# We are going to use fav_number as an argument to predict retweet_count
# Divide the training set and test set
set.seed(123)
trainIndex <- sample(1:nrow(twitter_data), 0.7*nrow(twitter_data))
trainData <- twitter_data[trainIndex,]
testData <- twitter_data[-trainIndex,]

# Random forest regression
model <- randomForest(retweet_count ~ fav_number, data=trainData, ntree=500)

# Visualize the result and draw a fitting line
ggplot(data=trainData, aes(x=fav_number, y=retweet_count)) +
  geom_point() +
  geom_smooth(method="lm", se=, color="red") +
  labs(title="Random Forest Regression", x="Favorite Number", y="Retweet Count")

# Make predictions using test set data
predictTest <- predict(model, newdata=testData)

# Plot the ratio of actual and predicted values
ggplot() +
  geom_point(data=testData, aes(x=fav_number, y=retweet_count), color="blue") +
  geom_point(data=data.frame(fav_number=testData$fav_number, Predicted=predictTest), aes(x=fav_number, y=Predicted), color="red", size=4) +
  labs(title="Random Forest Regression Evaluation", x="Favorite Number", y="Prediction")

# Output model evaluation indicators
print(model)

