import numpy as np

#This information was obtained from https://numpy.org/devdocs user guide

### Numpy Arrays

#Difference between a python list and a numpy list.
# - Python list can contain a number of data types and some methods of manipulation
# - Numpy array can contain only numbers but has a variaty of bultin operations
# - for efficiently manipulating the data inside
# - Numpy arrays are much faster and more compact
# - These arrays can be indexed by a tuple, a bool or an int

#Terminology
# - Numpy arrays are all of the same type known as the numpy dtype
# - The number of dimmentions is known as the rank
# - The size of the array in length and width is known as the shape (tuple)
# - 1D = Vector
# - 2D = Matrix
# - 3D = Tensor

numpy_array = np.array([1,2,3,4,5])

two_dimmentional_list = np.array([[1,2,3], [4,5,6],[7,8,9]])

#Example
print("Properties of 1D and 2D numpy arrays")
print(numpy_array.dtype)
print(numpy_array.shape)
print(two_dimmentional_list.dtype)
print(two_dimmentional_list.shape)

print("Creating basic arrays differently")
# Array operations
# - Array filled with zeros
print(np.zeros(2))

# - Array filled with zeros
print(np.ones(5))

# - Empty array. This behavior is to be filled with radom numbers. But ensure
# - to set each element before use
print(np.empty(4))

# - Create an array with a range of elements, this operates the same as range in standard python
print(np.arange(4))

print(np.arange(100, 1000, 50))

# - Use linspace to create an evenly distributed list
# - between start and end specifying the num of elements

linspace_array = np.linspace(0,10, num=5)
print(linspace_array)

# Sorting
print(np.sort(linspace_array))

# - argsort allows for more control over the algorithm used
mergesort_list = np.argsort(linspace_array,axis=0,kind='mergesort')
# - lexsort is used to sort on multiple keys

#Concatonation
first_array = np.array([1,2,3,4])
second_array = np.array([5,6,7,8])

third_array = np.concatenate((first_array,second_array))

print("Concatonated Array")
print(third_array)
print(third_array.ndim)
print(third_array.size)
print(third_array.shape)

print("Reshape Array")
print(third_array.reshape(4,2))
print(third_array.ndim)
print(third_array.size)
print(third_array.shape)

print(third_array.reshape(1,third_array.size)[0])
print(third_array[third_array < 3])

print("Stacking two existing arrays")
first = np.array([[1,1],[2,2],[3,3]])
second = np.array([[4,4],[5,5],[6,6]])
#Vertical stack
print(np.vstack((first,second)))
#Horizontal stack
print(np.hstack((first,second)))


print("Split 2D into 3 arrays")
#Here we create a 2D array with the range function
#Use the hsplit to split the array and the final param 3 means split into 3 arrays
#Note: the arrays must be equal size, in other words the array size must be
#evenly divisible by the number of arrays
print(np.hsplit(np.array([np.arange(1,13),np.arange(13,25)]),3))
# Can also specify the columns at which you need to split from
print(np.hsplit(np.array([np.arange(1,13),np.arange(13,25)]),(3,4)))


print("Modifications and Deep copy")
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = a[0,:]
b1[0] = 99
print(b1 )
print(a)
b1[0] = 1

b1 = a[0].copy()
print(b1)
b1[0] = 99
print(b1)
print(a)

#NB
# When creating a variable via reference, you need to be aware
# the origional will be manipul;ated along side the new variable

print("Basic array operations")
#Add the contents of two arrays
data = np.array([1,2])
ones = np.ones(2,dtype=int)
print(data+ones)
#All other arithmetic operations
print(data-ones)
print(data*data)
print(data/data)


#Sum the axis
b = np.array([[1,1],[2,2]])
print(b.sum(axis=0))
print(b.sum(axis=1))

#axis 0 is x axis
#axis 1 is y axis

#Boradcasting is the numpy mechanism of performing an action on every cell
print(b*5)


print("Aggregation")
numpy_array = np.array([1,2,3,4,5,6,7,56,4,3,23,23,2,12,1,4,5,3,2,235,235,23,12,34,213,123,125])
print(np.sort(numpy_array))
print(numpy_array.max())
print(numpy_array.min())
print(numpy_array.sum())
print(numpy_array.mean())
print(numpy_array.std())
print(numpy_array.prod())
