#NumPy is a python library
#used for workking with arrays
# short for "Numarical Python"

# it also has funtions working in domain of 
# linear algebra , fourier transform, and matrices. 

# created by Travis Oliphant
#NumPy aims to provide an array object that is up to 
# 50x faster than traditional Python lists

# ................contents..............
          # Intro
          # getting started
          # Creating arrays
          # Array Indexing
# .........................................
#Installation of NumPy
#.............pip install numpy.......

#importing the numpy library under the 'np' alias
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

#Checking NumPy Version
print(np.__version__)

#creating a NumPy ndarray object
# array object in NumPy is called ndarray
print(type(arr))

arr1 = np.array((3,9,6,8))
print(arr1)

#Dimensions in Arrays

# 0 - D Arrays or Scalars
arr2 = np.array(42)
print(arr2)

# 1 - D Arrays 0r Uni-Dimentional array
arr3 = np.array([4,5,6,7,8])
print(arr3)

#NumPy has a whole sub module dedicated towards 
# matrix operations called numpy.mat

# 2 - D Arrays
arr4 = np.array([[1,22,3,],[44,5,3]])
print(arr4)

# 3 - D arrays
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr5)

#Check number of dimensions
print(f"arr2 is a {arr2.ndim} dimension array")
print(f"arr3 is a {arr3.ndim} dimension array")
print(f"arr4 is a {arr4.ndim} dimension array")
print(f"arr5 is a {arr5.ndim} dimension array")

#Higher Dimensional Arrays
#you can define the number of dimensions 
# by using the 'ndmin' argument.

arr6 = np.array([1,2,3,4],ndmin=5)
print(arr6)
print(f"no of dimentions for arr6 is: {arr6.ndim}")

#Numpy array Indexing/accessing a array element
arr7 = np.array([1, 2, 3, 4])
print(arr7[1])
print(arr7[2] + arr7[3])

#Access 2-D Arrays
arr8 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr8[0, 1])
print('5th element on 2nd row: ', arr8[1, 4])

#Access 3-D Arrays
arr9 = np.array(
    [
    [                                         # 1st dimension
                [                             # 2nd dimension
                     [1, 2, 3], [14, 15, 16]  # 3rd dimension
                ]
                , 
                [
                     [7, 8, 9], [10, 11, 12]
                ]
    ],
    [                                         # 1st dimension
                [                             # 2nd dimension
                     [11, 21, 31], [14, 15, 16]  # 3rd dimension
                ]
                , 
                [
                     [7, 8, 9], [10, 11, 12]
                ]
    ]
    ]
)
print(f"no of dimentions for arr9 is: {arr9.ndim}")
print(arr9[0,0, 1, 2])
print(arr9[1,1, 0, 2])

#Negative Indexing
arr10 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr10[1, -1])