import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar
img = cv2.imread('enisaa.jpeg',0)

# Hitung histogram
hist,bins = np.histogram(img.flatten(),256,[0,256])

# Menghitung kumulatif histogram
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

# Menampilkan gambar dan histogram asli
plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('Gambar Asli')
plt.xticks([]), plt.yticks([])

plt.subplot(222)
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.title('Histogram Asli')
plt.xlim([0,256])

# Menampilkan gambar dan histogram setelah equalisasi
equ = cv2.equalizeHist(img)
plt.subplot(223)
plt.imshow(equ, cmap='gray')
plt.title('Gambar setelah Equalisasi')
plt.xticks([]), plt.yticks([])

plt.subplot(224)
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.title('Histogram setelah Equalisasi')
plt.xlim([0,256])

plt.show()