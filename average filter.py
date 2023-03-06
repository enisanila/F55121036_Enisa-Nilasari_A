import cv2
import numpy as np

# load the image
img = cv2.imread('enisaa.jpeg')

# define the kernel size for the average filter
kernel_size = (3, 3)

# create the kernel for the average filter
kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])

# apply the average filter to the image
filtered_img = cv2.filter2D(img, -1, kernel)

# display the original and filtered images side by side
combined_img = np.hstack([img, filtered_img])
cv2.imshow('Original vs Filtered', combined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




