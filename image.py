import cv2
import numpy as np
img = cv2.imread('1.jpg')

h,w=img.shape[:2]
start_row,start_col = int(h*.25),int(w*.25)
end_row,end_col = int(h*.9),int(w*.5)
cropped = img[start_row:end_row,start_col:end_col]

cv2.imshow('original',img)
cv2.waitKey(0)
cv2.imshow('cropped',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
