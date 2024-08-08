import cv2
import random
import numpy as np

img=cv2.imread("coffee.jpg",0)
face=cv2.imread("coffeeMug.jpg",0)
h, w = face.shape
result=cv2.matchTemplate(img,face,cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
location=(max_loc[0],max_loc[1])
bottom_right=(location[0]+w,location[1]+h)
cv2.rectangle(img,location,bottom_right,0,5)
cv2.imshow("match",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
'''

cv2.destroyAllWindows()

