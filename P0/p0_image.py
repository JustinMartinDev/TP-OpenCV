import cv2
import os
import sys
from matplotlib import pyplot as plt

#Affichage de l'environnement d'execution (version, répertoire de travail, ...)
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

print("OPENCV Version =", cv2.__version__)

rep_cour = os.getcwd()
print(rep_cour)

#Lecture de l'image et convertion en niveau de gris
img = cv2.imread('data/boats.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Calcule une nouvelle image avec la methode de laplace pour détecter les contours
laplacian = cv2.Laplacian(img, cv2.CV_64F)

#Calcule deux nouvelles images avec la methode Sobel (avec dérivé en x puis en y) pour détecter les contours
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

#Affichage du graphique contenant l'image de base ainsi que les 3 images issues de la detection de contours
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()