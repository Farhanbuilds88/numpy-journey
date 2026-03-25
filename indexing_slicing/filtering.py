#boolean indexing
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr>25])
print(arr[arr<30])

arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr_2d[arr_2d > 5])

arr_3d = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])
print(arr_3d[arr_3d > 5])
print(arr_3d[arr_3d % 2 == 0])
print(arr_3d[(arr_3d > 5) & (arr_3d < 10)])