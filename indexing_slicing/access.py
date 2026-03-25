import numpy as np
arr=np.array([10,23,45,67,76])
print(arr[0])
print(arr[1])
print(arr[-1])

arr_2d=np.array([[1,2,3],
                 [2,4,5]])
print(arr_2d[1,2])
print(arr_2d[0,1])

arr_3d = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])
print(arr_3d[0,0,0])