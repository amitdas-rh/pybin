#
# Date Aug 2020
# Iterating using numpy
#

import numpy as np

# version
print("Numpy version : " + np.__version__)

# 0-D, 1-D, 2-D, 3-D arrays defined
arr0d = np.array(99)
arr1d = np.array([99, 199, 299, 399, 499, 599])
arr2d = np.array([[99, 199, 299], [100, 200, 300]])
arr3d = np.array([[[1000, 2000, 3000], [999, 2999, 3999]], [[001, 002, 003], [599, 688, 777]]])

# Create empty list
lx = []

# User input for list
def usrentr():
    usrv = int(raw_input("Enter list size : "))  # format for v2.7 python
    for x in range(0, usrv):
        val = int(raw_input("~> "))
        lx.append(val)
    print("Done")
    print(lx)

# converting list to array
def aryconv():
    ary = np.array(lx)
    print("\nConverted to array " + str(ary))
    return ary

# Checking odd even
def odevn(ary):
    odc = 0  # type: int
    evnc = 0
    for nbr in ary:
        if (nbr % 2) == 0:   # check even
            print("~> {0} is even".format(nbr))
            evnc += 1
        else:
            print("~> {0} is odd".format(nbr))
            odc += 1
    print("\n Total {0} even number and {1} odd number in the array".format(evnc, odc))

# Call user entry
usrentr()

# Convert and return array
newary = aryconv()

# Check odd even in array
odevn(newary)
#EOF