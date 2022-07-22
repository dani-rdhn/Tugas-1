import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

image = plt.imread("pas foto (1).jpg")

plt.imshow(image)                           # Image asli
plt.show()    

plt.hist(image.ravel())                     # Histogram asli
plt.show()

img_pil = Image.fromarray(np.uint8(image))
img_pil = ImageOps.equalize(img_pil)
imgNp =np.asarray(img_pil) 

plt.imshow(imgNp)                           # Image setelah equalize
plt.show()

plt.hist(imgNp.ravel())                     # Histogram setelah equalize
plt.show()