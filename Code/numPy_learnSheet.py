import numpy as np
import pandas as pd
'''
l = list(range(100000))
a = np.arange(100000)           #just like using range syntax

print(a)


my_list = [[1,2,3,4,5],[6,7,8,9,10]]
np_array = np.array(my_list)

print(my_list*2)                #while original list doubling its array...
print(np_array*2)               #numPy can double its value
'''


arr = np.arange(100)           #when the array less than 1001 data, it will display all the data
arr_554 = arr.reshape(5,5,4)
randint_arr = np.random.randint(0,100,10)
'''
print(arr)
print(randint_arr)
print(np.max(randint_arr))      #same as randint_arr.max()
print(np.min(randint_arr))  
'''
print(arr)
print(arr_554)
print(arr.argmax())             #syntax to locate the position of highest number on array
