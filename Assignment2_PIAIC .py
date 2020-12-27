#Assignment 02
#Humaira Rana Anwar PIAIC142136
# In[1]:


import numpy as np


# In[2]:


#Question 1
arr = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
arr


# In[ ]:





# In[7]:


#Question 2
x = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
y = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
np.vstack((x,y))


# In[8]:


#Question 3
np.hstack((x,y))


# In[10]:


#Question 4
array1d = arr.ravel()
array1d


# In[12]:


#Question 5
arr2 = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9],[10,11,12,13,14]])
newarr = arr2.reshape(-1)
newarr


# In[13]:


#Question 6
arr3 = newarr.reshape(5,3)
arr3


# In[17]:


#Question 07
arr4 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
array_sq = arr4 * arr4
array_sq


# In[20]:


#Question 08
arr5 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30]])
array_mean = np.mean(arr5)
array_mean


# In[21]:


#Question 09
array_std = np.std(arr5)
array_std


# In[22]:


#Question 10
array_median = np.median(arr5)
array_median


# In[23]:


#Question 11
array_transpose = arr5.transpose()
array_transpose


# In[26]:


#Question 12
arr6 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
array_trace = np.trace(arr6)
array_trace


# In[27]:


#Question 13
arr_det = np.linalg.det(arr6)
arr_det


# In[30]:


#Question 14
per_5 = np.percentile(arr6,5)
per_95 = np.percentile(arr6,95)
print(per_5,per_95)


# In[31]:


#Question 15
check = np.isnan(arr6)
check


# In[ ]:




