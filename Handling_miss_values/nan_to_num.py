import numpy as np
arr=np.array([12,3,np.nan,4,np.nan,6])
print(np.isnan(arr))
cleaned_array=np.nan_to_num(arr,nan=100)
print(cleaned_array)