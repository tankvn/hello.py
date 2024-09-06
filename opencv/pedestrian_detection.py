## [imports]
import cv2
## [imports]

ped_cascade = cv2.CascadeClassifier('data/haarcascade_fullbody.xml')
img = cv2.imread('media/pexels-caffeine-28177648.jpg')
 
 
image = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
pedestrians = ped_cascade.detectMultiScale(image)
    
for (x,y,w,h) in pedestrians :
    cv2.rectangle(image,(x ,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("Display window", image)
cv2.waitKey(0)
cv2.destroyAllWindows()