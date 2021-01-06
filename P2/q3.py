import cv2
import numpy as np
from matplotlib import pyplot as plt

imgZebre = cv2.imread('../data/zebre.jpg')
imgSubran = cv2.imread('../data/suzan.jpg')

kernelY = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")
# construct the Sobel y-axis kernel

kernelX = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")

imgZebre_filtered = cv2.filter2D(imgZebre, -1, kernelX)
imgSuzan_filtered = cv2.filter2D(imgSubran, -1, kernelY)

# AffichAge du graphique contenant les images de base ainsi que les images issue du traitement
plt.subplot(2, 2, 1), plt.imshow(imgZebre, cmap='gray')
plt.title('Original zebre'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(imgZebre_filtered, cmap='gray')
plt.title('With filter'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(imgSubran, cmap='gray')
plt.title('Original suzan'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(imgSuzan_filtered, cmap='gray')
plt.title('With filter'), plt.xticks([]), plt.yticks([])
plt.show()
