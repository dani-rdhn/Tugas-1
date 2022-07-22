#!/usr/bin/env python
# coding: utf-8

# In[1]:


# inisialisasi import numpy dan matplotlib
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


get_ipython().system(' curl -O https://images.app.goo.gl/4sNfZrcyyxwyvXzH6')


# In[2]:


# kita baca gambar
#! dir *.jpg
img = plt.imread('E:\\pictures\\4Web\\4webBajo\\padar1.jpg')
plt.imshow(img)


# In[3]:


# liat tipe gambarnya--> ternyata numpy array
type(img)


# In[4]:


#ukuran array -- ternyata array 3 dimensi x, y, dan nilai rgb/warna nya
img.shape


# In[5]:


# konversi ke format PIL
img_pil = Image.fromarray(np.uint8(img)) # konversi ke format PIL, data pixel menjadi unsigned integer
img_pil =ImageOps.equalize(img_pil)      # equalize salah satu teknik image processing untuk enhance contrast


# In[6]:


plt.imshow(img_pil) # tunjukkin


# In[7]:


img2 =np.asarray(img_pil) # kembalikan ke format numpy
plt.imshow(img2)


# In[9]:


# plot histogram.. harus di flatkan dulu.. 
plt.hist(img2.ravel()) # ravel fungsi untuk flatten mendatarkan array 3d


# In[ ]:


# apa yang sudah dipelajari
# baca image dgn matplotlib
# plotting/displaying image
# konver ke format PIL
# equalizing histogram
# konvert kembali ke numpy
# histograms nilai piksel dgn matplotlib
# diambil dari https://www.youtube.com/watch?v=yM229XVkdOA

