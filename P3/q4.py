import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../data/cellules.png')


binary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

contours, h = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(binary, contours, 1, (0, 0, 255), 1)
nb_cel = len(contours)

plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(binary)
plt.title("Nb cellules = "+str(nb_cel)), plt.xticks([]), plt.yticks([])
plt.show()
