import numpy as np

row_size =30000
column_size =30000
arr1 = np.random.rand(row_size,column_size)
arr2= np.random.rand(row_size,column_size)
arr3=np.random.rand(row_size,column_size)

print(np.matmul(arr1,arr2,arr3))