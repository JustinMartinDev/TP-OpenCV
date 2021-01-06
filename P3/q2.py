# Image Processing with OpenCV

import cv2
from matplotlib import pyplot as plt

img_1 = cv2.imread('../data/jeu1.jpg')
img_2 = cv2.imread('../data/jeu2.jpg')

diff = cv2.absdiff(img_1, img_2)
ret, diff_inv = cv2.threshold(diff, 150, 255, cv2.THRESH_BINARY_INV)

plt.subplot(1, 3, 1), plt.imshow(img_1, cmap='gray')
plt.title('image 1'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(img_2, cmap='gray')
plt.title('image 2'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(diff_inv, cmap='gray')
plt.title('diff inv'), plt.xticks([]), plt.yticks([])
plt.show()
