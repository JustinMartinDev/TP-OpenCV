#Import de librairie
import cv2

#ne sert à rien
def frame_processing(imgc):
     return imgc

#Lecture de la vidéo (stockage des données dans une variable)
cap = cv2.VideoCapture('data/jurassicworld.mp4')

#Boucle permettant de traiter toutes les frames de la vidéo
while (True):

    #Récupére la "prochaine" frame
    ret, frame = cap.read()

    #Test si la vidéo est finie et donc pas de frame à trater
    if ret == True:
        #copy la frame pour la convertir en niveau de gris
        img = frame.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #Ne fait rien (pour le moment)
        gray = frame_processing(gray)

        #affiche la frame avant traitement et une fois traité
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