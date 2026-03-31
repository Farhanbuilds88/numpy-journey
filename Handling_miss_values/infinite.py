import numpy as np
arr=np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr))

arr = np.array([10, 20, np.inf, 40])
print(np.isinf(arr))

arr = np.array([-5, -10, -np.inf, 15])
print(np.isinf(arr))