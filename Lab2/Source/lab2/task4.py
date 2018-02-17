#importing numpy
import numpy as np
#range is 0-20 and the size of array is 15
x = np.random.randint(0, 20, 15)
print("Original array:")
print(x)
#Using Argmax we can get the most repeated value in array
print("Most frequent value in the array:")
print(np.bincount(x).argmax())
/Users/rakeshreddypallepati/PycharmProjects/lab2/task4.py