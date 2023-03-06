import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca citra
img = cv2.imread('enisaa.jpeg',0)

# membuat histogram
hist,bins = np.histogram(img.flatten(),256,[0,256])

# menampilkan histogram
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.show()
