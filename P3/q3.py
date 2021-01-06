import cv2


def frame_processing(imgc):
    ret, frame = cap.read()
    img_next_frame = frame.copy()
    img_next_frame_gray = cv2.cvtColor(img_next_frame, cv2.COLOR_BGR2GRAY)
    if ret == True:
        diff = cv2.absdiff(imgc, img_next_frame_gray)
        ret, diff_inv = cv2.threshold(diff, 127, 255, cv2.THRESH_BINARY)
        diff_inv_dilated = cv2.dilate(diff_inv, (5, 5), iterations=1)
        return diff_inv_dilated
    else:
        return imgc


cap = cv2.VideoCapture('../data/jurassicworld.mp4')

while (True):

    ret, frame = cap.read()

    if ret == True:
        img = frame.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray = frame_processing(gray)

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
