import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

image = plt.imread("99810.jpg")
img_pil = Image.fromarray(np.uint8(image))
img_pil = ImageOps.equalize(img_pil)
plt.imshow(img_pil)
# plt.imshow(image)
plt.show()

# img2 = np.asarray(img_pil)
# plt.imshow(img2)
# plt.hist(img2.ravel())

# img.shape()




# image = plt.imread("99810.jpg")

# # plt.imshow(image)                         # Image
# # plt.show()                                

# # plt.hist(image.ravel())                   # Histogram
# # plt.show()

# img_pil = Image.fromarray(np.uint8(image))
# img_pil = ImageOps.equalize(img_pil)
# imgNp =np.asarray(img_pil) # kembalikan ke format numpy

# plt.imshow(imgNp)                           # Image setelah equalize
# plt.show()

# # plt.hist(imgNp.ravel())                   # Histogram setelah equalize
# # plt.show()