# Mon script OpenCV : Video_processing
# Import de librairie
import cv2

def frame_processing(imgc):
    img_sobel_x= cv2.Sobel(imgc, cv2.CV_64F, 1, 0, ksize=3)
    img_sobel_y= cv2.Sobel(imgc, cv2.CV_64F, 0, 1, ksize=3)

    abs_grad_x = cv2.convertScaleAbs(img_sobel_x)
    abs_grad_y = cv2.convertScaleAbs(img_sobel_y)
    imgc = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
   # img_sobel=  cv2.Canny(imgc, 150, 250)
    return imgc

# Lecture de la vidéo (stockage des données dans une variable)
cap = cv2.VideoCapture('../data/jurassicworld.mp4')

# Boucle permettant de traiter toutes les frames de la vidéo
while (True):

    # Récupére la "prochaine" frame
    ret, frame = cap.read()

    # Test si la vidéo est finie et donc pas de frame à trater
    if ret == True:
        # copy la frame pour la convertir en niveau de gris
        img = frame.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Ne fait rien (pour le moment)
        gray = frame_processing(gray)

        # affiche la frame avant traitement et une fois traité
        cv2.imshow('MavideoAvant', frame)
        cv2.imshow('MavideoApres', gray)

    else:
        print('video ended')
        break

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
