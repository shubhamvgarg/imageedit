import cv2
import numpy as np
img = cv2.imread('1.jpg')

cv2.imshow('oiw',img)

cv2.waitKey(0)
img_scale = cv2.resize(img,None,fx=2,fy = 2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("new",img_scale)
cv2.waitKey(0)
cv2.destroyAllWindows()
