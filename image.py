import cv2
import numpy as np
def nothing(x):
    pass
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar("R",'image',0,255,nothing)
cv2.createTrackbar("G",'image',0,255,nothing)
cv2.createTrackbar("B",'image',0,255,nothing)
switch = '0 : OFF \n 1 : ON'
cv2.createTrackbar(switch,'image',0,1,nothing)
while True:
    cv2.imshow('image',img)
    if cv2.waitKey(1)==13:
        break
    r =cv2.getTrackbarPos('R','image')
    g =cv2.getTrackbarPos('G','image')
    b =cv2.getTrackbarPos('B','image')
    s =cv2.getTrackbarPos(switch,'image')

    if s==0:
        img[:]=0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()

    
device = cv2.VideoCapture(0)
while True:
    ret,frame = device.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lr = np.array([110,50,50])
    ur = np.array([130,250,250])
    mask = cv2.inRange(hsv,lr,ur)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("a",mask)
    cv2.imshow("b",result)
    cv2.imshow("c",frame)
    if cv2.waitKey(1)==13:
        break
device.release()
cv2.destroyAllWindows()