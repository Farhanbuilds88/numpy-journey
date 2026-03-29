#it gives how many rows and columns an array has
import numpy as np
arr_2d=np.array([[1,2,3],
                 [4,5,6]])
print(arr_2d.shape)

arr_3d=np.array([[[2,3,4,5],
          [3,4,5,6],
          [1,3,4,5]],
   [
      [2,3,4,5],
      [3,4,5,6],
      [1,3,4,5]
   ]
          ])
print(arr_3d.shape)