import numpy as np

print("Numpy version : " + np.__version__)
arr = np.array([1, 2, 3])
print("Numpy module type: " + str(type(arr)))

print("Checking....")
print(arr)

# converting list to array
tmptuple = ("Sydney", "Singapore", "Mumbai")
print("\nConverting list to array: ")
newarr = np.array(tmptuple)
print(newarr)

# 2-D array
print("\n====Creating Dimension array===\n")
#arr2d = np.array([[100, 200, 300], [99, 199, 299]])
#print(arr2d)

# 0-D, 1-D, 2-D, 3-D arrays defined
arr0d = np.array(99)
arr1d = np.array([99, 199, 299, 399, 499, 599])
arr2d = np.array([[99, 199, 299], [100, 200, 300]])
arr3d = np.array([[[1000, 2000, 3000], [999, 2999, 3999]], [[001, 002, 003], [599, 688, 777]]])

# ndim gives array dimension value
print(str(arr0d) + " is " + str(arr0d.ndim) + " Dimension\n")
print(str(arr1d) + " is " + str(arr1d.ndim) + " Dimension\n")
print(str(arr2d) + " is " + str(arr2d.ndim) + " Dimension\n")
print(str(arr3d) + " is " + str(arr3d.ndim) + " Dimension\n")

# Fetching values from the arrays dimension
print("===Retrieving arrays value===")
print("\n1-D second value : " + str(arr1d[1]))
print("\n1-D second and third value : " + str(arr1d[1]) + " " + str(arr1d[2]))

# summation from the array
x = arr1d[1] + arr1d[2]
print("\nSum of 1-Ds second and third value = " + str(x))

# Fetching 3rd dim value
print("\n3rd element from 2-D Dimention : " + str(arr2d[1, 2]))

# Fetching 2nd element of 3rd array from 3-D
print("\nLast element of 3-D array is :" + str(arr3d[1, 1, 2]))

# Fetching second last element
print("\nSecond last element of 3-D array is :" + str(arr3d[1, 1, -2]))

#print("1-D second value : " + str(arr1d[1]))
#print("1-D second value : " + str(arr1d[1]))
#print("1-D second value : " + str(arr1d[1]))

# Slice
print("\nAll last 3 elements in 1-D : " + str(arr1d[3:]))
print("\nAll 2nd to 5th elements in 1-D : " + str(arr1d[2:6]))
print("\nAll first 3 elements in 1-D : " + str(arr1d[:3]))

# 3-D slice
print("\n3-D slice : " + str(arr3d[1:2, 0:1, 1:2]))

# EOF


