
# coding: utf-8

# In[3]:


import numpy as np
import sys
import time


# In[4]:


data = [i for i in range(1,100001)]
np_data = np.array(data)


# In[5]:


sys.getsizeof(data)


# In[6]:


sys.getsizeof(np_data)


# In[11]:


data = []

data_1 = range(1,10000001)
data_2 = range(1,10000001)

start = time.time()

for i in range(len(data_1)):
    data.append(data_1[i] + data_2[i])
    
end = time.time()

total_time =  end - start
print("Total time taken is",total_time)


# In[12]:


len(data)


# In[13]:


np_data_1 = np.arange(1,10000001)
np_data_2 = np.arange(1,10000001)

start = time.time()

np_data = np_data_1 + np_data_2

end = time.time()

total_time =  end - start
print("Total time taken is",total_time)


# In[15]:


len(np_data) == len(data)

