# ------------------- SOM TRAINING ---------------------------

#choose the variables with which to train the SOM
#the following selects column 2,4,5,8
data_train <- data_raw[, c(2,4,5,8)]
data_train <- data_raw

# now train the SOM using the Kohonen method
data_train_matrix <- as.matrix(scale(data_train))
names(data_train_matrix) <- names(data_train)
require(kohonen)
som_grid <- somgrid(xdim = 10, ydim=10, topo="hexagonal")  

# Train the SOM model!
system.time(som_model <- som(data_train_matrix, 
                             grid=som_grid, 
                             rlen=1000, 
                             alpha=c(0.9,0.01), 
                             n.hood = "circular",
                             keep.data = TRUE ))

rm(som_grid, data_train_matrix)

