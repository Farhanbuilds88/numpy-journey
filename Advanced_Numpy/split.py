import numpy as np
arr = np.array([1,2,3,4,5,6])
result = np.split(arr, 2)
print(result)

arr = np.array([10,20,30,40,50,60])

result = np.split(arr, [2, 4])

print(result)