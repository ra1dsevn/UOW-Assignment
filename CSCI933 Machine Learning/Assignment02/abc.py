# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create  data
raw_data_x = [[3.393533211, 2.331273381],
              [3.110073483, 1.781539638],
              [1.343808831, 3.368360954],
              [3.582294042, 4.679179110],
              [2.280362439, 2.866990263],
              [7.423436942, 4.696522875],
              [5.745051997, 3.533989803],
              [9.172168622, 2.511101045],
              [7.792783481, 3.424088941],
              [7.939820817, 0.791637231]]
raw_data_y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# convert list object to np.array object
x_train = np.array(raw_data_x)
y_train = np.array(raw_data_y)
print('123')
# test point
demo_point = np.array([8.093607318,3.365731514])

plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)
plt.plot(demo_point[0], demo_point[1], 'r*', markersize=10)