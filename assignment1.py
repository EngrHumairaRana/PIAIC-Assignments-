#Assignment 01
#Humaira Rana Anwar PIAIC142136

#Difficulty Level: Beginner
#-------------------------

# 1. Import the numpy package under the name np
import numpy as np

# 2. Create a null vector of size 10
x = np.zeros(10)

# 3. Create a vector with values ranging from 10 to 49
v = np.arange(10,50)

# 4. Find the shape of previous array in question 3
v.shape

# 5. Print the type of the previous array in question 3
print(v.dtype)

# 6. Print the numpy version and the configuration
print(np.__version__)
print(np.show_config())

# 7. Print the dimension of the array in question 3
print(v.ndim)

# 8. Create a boolean array with all the True values
a = np.ones((1, 2), dtype=bool)

# 9. Create a two dimensional array
b = np.array([(1,2,3), (4,5,6)])

# 10. Create a three dimensional array
array_3d = np.ones((2,2,2))



#Difficulty Level: Beginner
#-------------------------

# 11. Reverse a vector (first element becomes last)
rev_v = v[::-1]

# 12. Create a null vector of size 10 but the fifth value which is 1
import numpy as np
arr1 = np.zeros(10)
arr1[4]=1

# 13. Create a 3x3 identity matrix
x = np.eye(3)

#14. Convert the data type of the given array from int to float
arr = arr.astype('float64') 

# 15. Multiply arr1 with arr2
arr1 = np.array([[1., 2., 3.], [4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
arr3 = np.multiply(arr1, arr2)

# 16. Make an array by comparing both the arrays provided above
arr4 = np.greater(arr1, arr2)

# 17. Extract all odd numbers from arr with values(0-9)
arr = np.array([1, 2, 3, 4, 5])
arr[arr % 2 == 1]

#18. Replace all odd numbers to -1 from previous array
arr = np.array([1, 2, 3, 4, 5])
arr[arr % 2 == 1] = -1

# 19. Replace the values of indexes 5,6,7 and 8 to 12
arr = np.arange(10)
arr[5]=12
arr[6]=12
arr[7]=12
arr[8]=12

# 20. Create a 2d array with 1 on the border and 0 inside
z = np.ones((5,5))
z[1:-1,1:-1]=0


#Difficulty Level: Medium
#-------------------------

# 21. Replace the value 5 to 12
arr2d = np.array([[1, 2, 3],
            [4, 5, 6], 
            [7, 8, 9]])
arr2d[1][1]=12

# 22. Convert all the values of 1st array to 64
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[0] = 64

#23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it
arr2d = np.array([[1, 2, 3],
            [4, 5, 6], 
            [7, 8, 9]])
sliced = arr2d[0]

# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it
arr2d = np.array([[1, 2, 3],
            [4, 5, 6], 
            [7, 8, 9]])
sliced = arr2d[1][1]

# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows
arr2d = np.array([[1, 2, 3],
            [4, 5, 6], 
            [7, 8, 9]])
arr2d[:2,2:]

# 26. Create a 10x10 array with random values and find the minimum and maximum values
arr = np.random.randn(10,10)
np.max(arr)
np.min(arr)

#27. Find the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)

#28. Find the positions where elements of a and b match
a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a==b)

#29. Find all the values from array data where the values from array names are not equal to Will
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
np.where(names!="Will")

#30. Find all the values from array data where the values from array names are not equal to Will and Joe
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
np.where((names != 'Joe') & (names != 'Will'))


# Difficulty Level: Hard
#-------------------------

# 31.Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.
arr = np.arange(1,16).reshape(5,3)

#32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.
arr = np.arange(1,17).reshape(2,2,4)

#33. Swap axes of the array you created in Question 32
np.swapaxes(arr,0,2)

#34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0
arr = np.arange(10)
arr_sq = np.sqrt(arr)
print(arr_sq)
np.where(arr_sq<0.5, 0,arr_sq)

#35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays
arr1 = np.random.randn(12)
arr2 = np.random.randn(12)
np.maximum(arr1, arr2)

#36. Find the unique names and sort them out!
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
unique_names = np.unique(names)
sorted_names = np.sort(unique_names)

#37. From array a remove all items present in array b
a = np.array([1,2,3,4,5]) 
b = np.array([5,6,7,8,9])
result = np.setdiff1d(a, b)

#38. Following is the input NumPy array delete column two and insert following new column in its place.
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = np.array([[10,10,10]])
array_del = np.delete(sampleArray, 1, 1)
final = np.insert(array_del,1,newColumn, 1)

#39. Find the dot product of the above two matrix
x = np.array([[1., 2., 3.], [4., 5., 6.]]) 
y = np.array([[6., 23.], [-1, 7], [8, 9]])
z = np.dot(x,y)

#40. Generate a matrix of 20 random values and find its cumulative sum
arr = np.random.randn(20)
sumarray = np.cumsum(arr)









