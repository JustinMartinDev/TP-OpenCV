import cv2
from matplotlib import pyplot as plt

#Lecture de l'image et convertion d'une copie en niveau de gris
img = cv2.imread('data/lisa.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#calcul de l'histograme des niveaux de gris
hist = cv2.calcHist([imgGray], [0], None, [256], [0, 256])

#Affichge du graphique contenant l'image de base ainsi que celle en niveaux de gris
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.imshow(imgGray,cmap = 'gray')
plt.title('Gray'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3),plt.plot(hist)
plt.show()

#Au point 1 il y'a beaucoup de pixels sombres, et en position 2 cela indique qu'il y'a peu de pixels claires