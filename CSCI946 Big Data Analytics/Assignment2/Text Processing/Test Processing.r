# Load necessary packages
library(tidyverse)
library(readr)
library(Matrix)
library(tm)
library(SnowballC)
library(wordcloud)

# Set the working directory and load Twitter data
twitter_data <- read.csv("twitter_user_data.csv", encoding = "latin1")

# Remove rows containing missing or NA values
twitter_data <- na.omit(twitter_data)

# Exclude rows with unknown or missing gender values
twitter_data <- twitter_data %>%
  filter(!is.na(gender) & gender != "unknown")

# Define a function to preprocess and extract features from text
text_features <- function(text) {
  # Convert all characters to lowercase
  text <- tolower(text)
  # Remove punctuation, numbers, and URLs
  text <- gsub("[[:punct:]]", " ", text)
  text <- gsub("[[:digit:]]", " ", text)
  text <- gsub("http\\S+", " ", text)
  # Split text into individual words (tokenization)
  text <- strsplit(text, " ")
  # Remove commonly used words (stop words)
  text <- lapply(text, function(x) x[!x %in% stopwords("english")])
  # Apply stemming to reduce words to their root form
  text <- lapply(text, function(x) wordStem(x, language = "english"))
  # Return a single vector of processed words
  unlist(text)
}

# Apply the feature extraction function to text and profile description
twitter_data$text_features <- lapply(twitter_data$text, text_features)
twitter_data$description_features <- lapply(twitter_data$description, text_features)

# Combine extracted features, sidebar color, and link color into one feature set
twitter_data$features <- mapply(c, twitter_data$text_features, twitter_data$description_features, 
                                twitter_data$sidebar_color, twitter_data$link_color, SIMPLIFY = FALSE)

# Convert the combined feature vector into a text corpus
corpus <- Corpus(VectorSource(unlist(twitter_data$features)))

# Generate a document-term matrix from the corpus
dtm <- DocumentTermMatrix(corpus)

# Convert the gender column into a factor for classification
twitter_data$gender <- factor(twitter_data$gender)

# Generate a word cloud visualization
set.seed(123)  # Ensure reproducibility
wordcloud(
  words = twitter_data$text, 
  max.words = 100,              # Limit the number of displayed words
  random.order = FALSE,         # Display most frequent words in the center
  colors = brewer.pal(8, "Dark2"), # Use a visually appealing color palette
  scale = c(3, 0.5)             # Adjust the word size scaling
)

# Add a title to the word cloud
title(main = "Word Cloud of Twitter User Data")
