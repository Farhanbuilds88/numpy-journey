import numpy as np
arr=np.array([12,3,np.nan,4,np.nan,6])
print(np.isnan(arr))

new_arr=np.array([23,4,5,7,8,np.nan,np.nan])
print(np.isnan(new_arr))  

new1=np.array([45,6,7,8,9,0,np.nan,np.nan,np.nan,34,5,6,7,8])
print(np.isnan(new1))
check_array=np.array([2,3,4,5,6,np.nan,56,np.nan,np.nan,45,6,7,8])
print(np.isnan(check_array))