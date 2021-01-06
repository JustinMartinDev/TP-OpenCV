# Image Processing with OpenCV

import cv2
from matplotlib import pyplot as plt

image_list = ['data/soleil.png', 'data/aqui.jpg']

index=1
for image_path in image_list:
    #Lecture de l'image et convertion en niveau de gris
    img = cv2.imread(image_path)
    if image_path.__contains__(".png") :
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    #calcul de l'histogramme des niveaux de gris
    hist = cv2.calcHist([imgGray], [0], None, [256], [0, 256])

    #Egalisation de l'histogramme / image
    imgEqualized = cv2.equalizeHist(imgGray)
    histEq = cv2.calcHist([imgEqualized], [0], None, [256], [0, 256])

    #Affichage
    plt.subplot(2, 2, 1), plt.plot(hist)
    plt.title('Histo'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2), plt.imshow(imgGray, cmap='gray')
    plt.title('Gray'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.plot(histEq)
    plt.title('Histo eq'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(imgEqualized, cmap='gray')
    plt.title('Equalized'), plt.xticks([]), plt.yticks([])
    plt.show()