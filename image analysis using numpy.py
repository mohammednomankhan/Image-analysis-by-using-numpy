
# coding: utf-8

# # image analysis using numpy

# ## import required libraries

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


# ## read image and store image in matrix

# In[2]:


image_data = misc.imread('4493425-hd-wallpapers-1080p.JPG') #image is loaded and stored as numpy ndarray

print(type(image_data)) 

print("\n shape of array : ",image_data.shape)

print(image_data)


# ## print image using matplotlib
# 

# In[3]:


plt.figure(figsize=(10,10))

plt.imshow(image_data)


# In[4]:


print('minimum value in image_data : ',image_data.min())
print('maximum value in image_data : ',image_data.max())


# 
# ## assign 0 to all values from row 200 to 400 to print a balck line
# 

# In[5]:


image_data[200:400,:] = 0 #assign 0 to all values from row 200 to 400

plt.figure(figsize=(10,10)) #changing figure size

plt.imshow(image_data) #show image


# ## creating white line by assigning 255 to every values from row 600 to 1000

# In[6]:


image_data = misc.imread('4493425-hd-wallpapers-1080p.JPG') #image is loaded and stored as numpy ndarray

image_data[600:1000,:] = 255

plt.figure(figsize=(10,10))

plt.imshow(image_data)


# ## removing green color from image by assigning 0 

# In[7]:


image_data = misc.imread('4493425-hd-wallpapers-1080p.JPG') #image is loaded and stored as numpy ndarray

image_data[:,:,1] = 0

print(image_data)

plt.figure(figsize=(10,10))

plt.imshow(image_data)


# ## changing green color intensity to highest by assigning 255 from row 200 to row 600 

# In[8]:


image_data = misc.imread('4493425-hd-wallpapers-1080p.JPG') #image is loaded and stored as numpy ndarray

image_data[200:600,:,1] = 255

print(image_data[200:600,:])

plt.figure(figsize=(10,10))

plt.imshow(image_data)


# ## changing all values to 0 which are less then 100

# In[9]:


image_data = misc.imread('4493425-hd-wallpapers-1080p.JPG') #image is loaded and stored as numpy ndarray

image_data[image_data<100] =0

plt.figure(figsize=(10,10))

plt.imshow(image_data)


# ## changing all the values to 0 of red layer which are greater then 50  

# In[10]:


image_data = misc.imread('4493425-hd-wallpapers-1080p.JPG') #image is loaded and stored as numpy ndarray

image_data[image_data[:,:,0]>50]  = 0

plt.figure(figsize=(10,10))

plt.imshow(image_data)


# ## changing all the values to 0 of red layer which are less then 150

# In[11]:


image_data = misc.imread('4493425-hd-wallpapers-1080p.JPG') #image is loaded and stored as numpy ndarray

selection = image_data[:, : ,0] < 150

image_data[selection] = 0

plt.figure(figsize=(10,10))

plt.imshow(image_data)


# ## changing values of columns from 1000 to 1500 of rows 200 to 400  to 120
# 
# 

# In[23]:


image_data = misc.imread('4493425-hd-wallpapers-1080p.JPG') #image is loaded and stored as numpy ndarray

image_data[200:400,1000:1500] = 120

plt.figure(figsize=(10,10))

plt.imshow(image_data)

