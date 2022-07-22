import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 

# open = pd.read_csv('bps-file (1).csv')
# x = open['x']
# y = open['y']

# plt.scatter(x, y, color='black')
# plt.show()
# ------------------------------------------------------------------------------------------

# harga = [10000, 20000, 30000]
# jumlah = [20, 30, 40]
# plt.scatter(harga, jumlah, color='black')
# plt.show()
# ------------------------------------------------------------------------------------------

# months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16,17,18,19,20,21,22,23,24]
# average_basket_size = [199000, 198200, 199800, 220050, 232100, 221000, 222800, 229000, 230000, 231000, 232700, 235500, 222800, 229000, 230000, 231000, 232700, 23550, 199000, 198200, 199800, 220050, 232100, 221000]

# plt.plot(months, average_basket_size, marker='o' )

# plt.title("Muhammad Ramadhan Muttaqqien_1202204096")

# plt.xlabel("Months")
# plt.ylabel("Average Basket Size")
# plt.show()
# ------------------------------------------------------------------------------------------

image = plt.imread("99810.jpg")
plt.imshow(image)
plt.show()