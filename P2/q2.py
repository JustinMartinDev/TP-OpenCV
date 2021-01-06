# Image Processing with OpenCV

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../data/boats.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#flou gaussien - masque median
imgGrayGaussianBlured = cv2.GaussianBlur(imgGray, (5, 5), 0)
imgGrayMedianBlured = cv2.medianBlur(imgGray, 5)


plt.subplot(2, 2, 1), plt.imshow(imgGray, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(imgGrayGaussianBlured, cmap='gray')
plt.title('Gaussian Blur (5x5)'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(imgGrayMedianBlured, cmap='gray')
plt.title('Median Blur (5x5)'), plt.xticks([]), plt.yticks([])
plt.show()