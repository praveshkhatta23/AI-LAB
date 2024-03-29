# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:34:34 2019

@author: Student
"""
import numpy as np  
arr = np.array( [[ 1, 2, 3], 
                 [ 4, 2, 5]] )    
print("Array is of type: ", type(arr)) 
print("No. of dimensions: ", arr.ndim) 
print("Shape of array: ", arr.shape)  
print("Size of array: ", arr.size)  
print("Array stores elements of type: ", arr.dtype) 
import numpy as np 
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
print ("Array created using passed list:\n", a) 
b = np.array((1 , 3, 2)) 
print ("\nArray created using passed tuple:\n", b) 
c = np.zeros((3, 4)) 
print ("\nAn array initialized with all zeros:\n", c) 
d = np.full((3, 3), 6, dtype = 'complex') 
print ("\nAn array initialized with all 6s.""Array type is complex:\n", d) 
e = np.random.random((2, 2)) 
print ("\nA random array:\n", e) 
f = np.arange(0, 30, 5) 
print ("\nA sequential array with steps of 5:\n", f)  
g = np.linspace(0, 5, 10) 
print ("\nA sequential array with 10 values between""0 and 5:\n", g)  
arr = np.array([[1, 2, 3, 4], 
                [5, 2, 4, 2], 
                [1, 2, 0, 1]]) 
newarr = arr.reshape(2, 2, 3) 
print ("\nOriginal array:\n", arr) 
print ("Reshaped array:\n", newarr)  
arr = np.array([[1, 2, 3], [4, 5, 6]]) 
flarr = arr.flatten() 
print ("\nOriginal array:\n", arr) 
print ("Fattened array:\n", flarr) 
import numpy as np  
arr = np.array([[-1, 2, 0, 4], 
                [4, -0.5, 6, 0], 
                [2.6, 0, 7, 8], 
                [3, -7, 4, 2.0]]) 
temp = arr[:2, ::2] 
print ("Array with first 2 rows and alternate""columns(0 and 2):\n", temp) 
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]] 
print ("\nElements at indices (0, 3), (1, 2), (2, 1),""(3, 0):\n", temp) 
cond = arr > 0
temp = arr[cond] 
print ("\nElements greater than 0:\n", temp) 
import numpy as np   
a = np.array([1, 2, 5, 3]) 
print ("Adding 1 to every element:", a+1) 
print ("Subtracting 3 from each element:", a-3) 
print ("Multiplying each element by 10:", a*10) 
print ("Squaring each element:", a**2) 
a *= 2
print ("Doubled each element of original array:", a)  
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 
print ("\nOriginal array:\n", a) 
print ("Transpose of array:\n", a.T) 
import numpy as np 
arr = np.array([[1, 5, 6], 
                [4, 7, 2], 
                [3, 1, 9]])  
print ("Largest element is:", arr.max()) 
print ("Row-wise maximum elements:",arr.max(axis = 1)) 
print ("Column-wise minimum elements:",arr.min(axis = 0)) 
print ("Sum of all array elements:",arr.sum())  
print ("Cumulative sum along each row:\n",arr.cumsum(axis = 1)) 
import numpy as np 
a = np.array([[1, 2], 
            [3, 4]]) 
b = np.array([[4, 3], 
            [2, 1]]) 
print ("Array sum:\n", a + b)  
print ("Array multiplication:\n", a*b) 
print ("Matrix multiplication:\n", a.dot(b)) 
import numpy as np 
a = np.array([0, np.pi/2, np.pi]) 
print ("Sine values of array elements:", np.sin(a)) 
a = np.array([0, 1, 2, 3]) 
print ("Exponent of array elements:", np.exp(a)) 
print ("Square root of array elements:", np.sqrt(a))
import numpy as np 
a = np.array([[1, 4, 2], 
                 [3, 4, 6], 
              [0, -1, 5]]) 
print ("Array elements in sorted order:\n",np.sort(a, axis = None))  
print ("Row-wise sorted array:\n",np.sort(a, axis = 1))  
print ("Column wise sort by applying merge-sort:\n",np.sort(a, axis = 0, kind = 'mergesort')) 
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]  
values = [('Siddharth', 2009, 8.5), ('Dhruv', 2008, 8.7),  
           ('Chinmoy', 2008, 7.9), ('Pravesh', 2009, 9.0)]
arr = np.array(values, dtype = dtypes) 
print ("\nArray sorted by names:\n",np.sort(arr, order = 'name'))
print ("Array sorted by grauation year and then cgpa:\n",np.sort(arr, order = ['grad_year', 'cgpa'])) 