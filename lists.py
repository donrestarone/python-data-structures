# import numpy library aliased as np
import numpy as np

# generate a normal distribution given 3 parameters
a = np.random.normal(55, 5.0, 10)

print (type(a))

listX = [1,2,3,4,5,6]
listX3rdIndexAndUp = listX[3:]
# print(listX3rdIndexAndUp)

listXLast2Indexes = listX[-2:]
print(listXLast2Indexes)

listOfLists = [listX, listX3rdIndexAndUp, listXLast2Indexes]

print(listOfLists)

# sorting


# use standard library function length as a custom sorting argument. Outputs the arrays sorted from smallest to largest 
listOfLists.sort(key=len)
print(listOfLists)


listX.sort(reverse=True)

print(listX)