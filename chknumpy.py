import numpy as np

print(np.__version__)
arr = np.array([1, 2, 3])
print("Numpy module type: " + str(type(arr)))

print("Checking....")
print(arr)

# converting list to array
tmptuple = ("Sydney", "Singapore", "Mumbai")
print("Converting list to array: ")
newarr = np.array(tmptuple)
print(newarr)

# 2-D array
print("\n====Creating Dimension array===")
#arr2d = np.array([[100, 200, 300], [99, 199, 299]])
#print(arr2d)

# 0-D, 1-D, 2-D, 3-D arrays defined
arr0d = np.array(99)
arr1d = np.array([99, 199, 299])
arr2d = np.array([[99, 199, 299], [100, 200, 300]])
arr3d = np.array([[[1000, 2000, 3000], [999, 2999, 3999]], [[001, 002, 003], [599, 688, 777]]])

# ndim gives array dimension value
print(str(arr0d) + " is " + str(arr0d.ndim) + " Dimension\n")
print(str(arr1d) + " is " + str(arr1d.ndim) + " Dimension\n")
print(str(arr2d) + " is " + str(arr2d.ndim) + " Dimension\n")
print(str(arr3d) + " is " + str(arr3d.ndim) + " Dimension\n")


# EOF
