import cv2
import numpy as np
import glob



def sharp_and_Contrast(image,path):
    cv2.imshow('Sample Image', image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
    image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
    alpha = 0.9# Contrast control (1.0-3.0)
    beta = 0 # Brightness control (0-100)
    adjusted = cv2.convertScaleAbs(image_sharp, alpha=alpha, beta=beta)
    cv2.imshow('Sharp & Contrast Image',adjusted)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite(path,adjusted)



folder_dir = "./images"
for file in glob.glob('./images/*.jpg'):
    path = str(file)
    img = cv2.imread(file)
    sharp_and_Contrast(img,path)

    
