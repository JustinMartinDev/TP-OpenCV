
import cv2
from matplotlib import pyplot as plt

#Lecture de l'image et conversion en niveau de gris
img = cv2.imread('../data/lisa.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

imgBlur5 = cv2.blur(imgGray, (5, 5))
imgBlur9 = cv2.blur(imgGray, (9, 9))
imgBlur15 = cv2.blur(imgGray, (15, 15))
imgBlurComplete = cv2.blur(imgGray, (494, 768))

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.imshow(imgBlur5,cmap = 'gray')
plt.title('blur 5x5'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3),plt.imshow(imgBlur9,cmap = 'gray')
plt.title('blur 9x9'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4),plt.imshow(imgBlur15,cmap = 'gray')
plt.title('blur 15x15'), plt.xticks([]), plt.yticks([])



plt.show()
