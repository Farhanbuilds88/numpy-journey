import numpy as np
ar_1d=([10,20,34,56])
print(ar_1d)

arr_2d=([[1,2,3,5],
        [2,4,5,7],
        [5,5,8,9]])
print(arr_2d)

matrix=np.array([[2,4,6],
                 [8,10,12]])
print(matrix)

temperature=[34.5,32.5,24.5,26]
total=0
for temp in temperature:
    total+=temp
print("the sum of the all value is :",total)
count=len(temperature)
average=total/count
print("the average is :",average)

python_list=[12,34,45,56]
total_sum=0
for i in python_list:
    total+=i
print("the sum of all values is",total_sum)
average_1=total/len(python_list)
print("the average is :",average_1)