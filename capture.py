import cv2 as cv
import os

cam = cv.VideoCapture(0)   
s, img = cam.read()
path = 'D:/xamppangel/htdocs/Marriyo/marriyo'
if s:
    cv.namedWindow("cam-test")
    cv.imshow("cam-test",img)
    cv.waitKey(0)
    #cv.destroyWindow("cam-test")
    #cv.imwrite(directory+"filename.jpg",img)
    imname=img[0][0][0]
    imname1=img[0][0][1]
    imname2=img[0][0][2]
    #print(imname)
    #print(imname1)
    #print(imname2)
    imagename=str(imname)+""+str(imname1)+""+str(imname2)+".jpg"
    #print(imagename)
    cv.imwrite(os.path.join(path , imagename), img)