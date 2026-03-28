import numpy as np
arr=np.array([1,2,3,4,5])
result=np.where(arr>3,100,0)
print(result)

marks=np.array([20,34,45,68])
new_marks=np.where(marks>30,100,50)
print(new_marks)