import cv2
from matplotlib import pyplot as plt

img_phone = cv2.imread('../data/phone.jpg', cv2.CV_8UC1)
img_vache = cv2.imread('../data/vache.jpg')

img_gauss = cv2.adaptiveThreshold(img_phone, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)
img_mean = cv2.adaptiveThreshold(img_phone, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)

plt.subplot(1, 3, 1), plt.imshow(img_phone, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 2), plt.imshow(img_gauss, cmap='gray')
plt.title('Binary Gaussian'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 3), plt.imshow(img_mean, cmap='gray')
plt.title('Binary Mean'), plt.xticks([]), plt.yticks([])
plt.show()
