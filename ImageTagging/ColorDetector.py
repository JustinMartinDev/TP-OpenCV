from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("../data/vache.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# reshape the image to be a list of pixels
image = image.reshape((image.shape[0] * image.shape[1], 3))

# cluster the pixel intensities 1 to have main color, 2 to have 2 main color, ....
clt = KMeans(n_clusters = 1)
clt.fit(image)

main_colors = clt.cluster_centers_.astype(int)
print("main color(s)", main_colors)