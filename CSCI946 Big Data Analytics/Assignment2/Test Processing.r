# Load necessary libraries
library(tidyverse)
library(tm)
library(SnowballC)
library(wordcloud)

# Read and clean data
twitter_data <- read.csv("twitter_user_data.csv", encoding = "latin1")
twitter_data <- na.omit(twitter_data) # Remove missing values
twitter_data <- twitter_data %>% filter(!is.na(gender) & gender != "unknown") # Exclude rows with unknown gender

# Clean text data to ensure valid UTF-8 encoding
clean_text <- function(text) {
  # Replace invalid characters and ensure UTF-8 encoding
  text <- iconv(text, from = "latin1", to = "UTF-8", sub = "")
  # Replace non-printable characters with a space
  text <- gsub("[^[:print:]]", " ", text)
  # Return cleaned text
  text
}

# Apply the cleaning function to text and description columns
twitter_data$text <- sapply(twitter_data$text, clean_text)
twitter_data$description <- sapply(twitter_data$description, clean_text)

# Define a function to preprocess and extract features from text
text_features <- function(text) {
  # Convert to lowercase and remove punctuation, numbers, and URLs
  text <- tolower(text)
  text <- gsub("[[:punct:]]", " ", text)
  text <- gsub("[[:digit:]]", " ", text)
  text <- gsub("http\\S+", " ", text)
  # Tokenize, remove stopwords, and stem words
  words <- unlist(strsplit(text, " "))
  words <- words[!words %in% stopwords("english")]
  words <- wordStem(words, language = "english")
  # Return processed words
  words[words != ""]
}

# Apply the feature extraction function to text and description
twitter_data$text_features <- lapply(twitter_data$text, text_features)
twitter_data$description_features <- lapply(twitter_data$description, text_features)

# Combine features into a single vector
twitter_data$features <- mapply(c, twitter_data$text_features, twitter_data$description_features, 
                                SIMPLIFY = FALSE)

# Remove empty feature sets
non_empty_features <- Filter(function(x) length(x) > 0, twitter_data$features)

# Convert features into a text corpus
corpus <- Corpus(VectorSource(non_empty_features))

# Preprocess the corpus
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords("english"))
corpus <- tm_map(corpus, stripWhitespace)

# Create a document-term matrix
dtm <- DocumentTermMatrix(corpus)

# Generate the word cloud
set.seed(123)
wordcloud(
  words = unlist(non_empty_features),  # Flatten the features into a single vector
  max.words = 100,
  random.order = FALSE,
  colors = brewer.pal(8, "Dark2"),
  scale = c(3, 0.5)
)
