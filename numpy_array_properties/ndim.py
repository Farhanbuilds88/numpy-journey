#it gives us dimension of an array
import numpy as np
arr_id=np.array([1,3,4])
print(arr_id.ndim)

arr_2d=np.array([[1,2,3,4]
                 ,[4,4,5,5]
                 ,[3,4,5,6]])
print(arr_2d.ndim)

arr_3d=np.array([[[1,3,4,5]
                  ,[2,4,5,1],
                  [2,7,8,4]]])
print(arr_3d.ndim)
#3d
first_array=np.array([[[2,3,4,5,6],[2,3,4,6,7],[3,4,5,6,6]],
                      [[2,3,4,5,8],[4,5,6,7,3],[4,5,6,7,3]]])
print(first_array.ndim)
print(first_array.size)
print(first_array.shape)