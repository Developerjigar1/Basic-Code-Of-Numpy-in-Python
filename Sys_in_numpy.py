
import numpy as np

#1d array
print("1D Array:")
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([1,2,3,4,5])

#2d array
print
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])


#3d array
print("3D Array:")
arr4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])

#display array 1

print("Array 1:", arr1)

#addition of arr1 and arr2
print("Addition:", arr1 + arr2)

#display 2d array
print("2D Array:\n", arr3)

#display 3d array
print("3D Array:\n", arr4)

#shape of arrays
print("Shape of all arrays:/n")
print("Shape of arr1:", arr1.shape)
print("Shape of arr3:", arr3.shape)
print("Shape of arr4:", arr4.shape)
print("Shape of arr2:", arr2.shape)

#data type of all arrays
print("Data type of all arrays:/n")
print("datatype of arr1-",arr1.dtype)
print("datatype of arr2-",arr2.dtype)
print("datatype of arr3-", arr3.dtype)
print("datatype of arr4-", arr4.dtype)

#size of all arrays
print("Size of all arrays:/n")
print("side of arr1-",arr1.size)
print("side of arr2-",arr2.size)
print("size of arr3-", arr3.size)
print("size of arr4-", arr4.size)

#number of dimensions of all arrays
print("Number of dimensions of all arrays:/n")
print("dimension of arr1-",arr1.ndim)
print("dimension of arr2-",arr2.ndim)
print("dimension of arr3-",arr3.ndim)
print("dimension of arr4-",arr4.ndim)

#itemsize of all arrays
print("Itemsize of all arrays:/n")
print("itemsize of arr1-",arr1.itemsize)
print("itemsize of arr2-",arr2.itemsize)
print("itemsize of arr3-",arr3.itemsize)
print("itemsize of arr4-",arr4.itemsize)


#nbytes of all arrays
print("Nbytes of all arrays:/n")
print("nbytes of arr1-",arr1.nbytes)
print("nbytes of arr3-",arr3.nbytes)
print("nbytes of arr4-",arr4.nbytes)

#create an array of zeros in a array of shape 3x4
print("Array of zeros with shape 3x4:")
np.zeros((3,4))

#create an array of ones in a array of shape 3x4
print("Array of ones with shape 3x:")
np.ones((3,5))