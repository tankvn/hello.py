## [imports]
import cv2 as cv
import sys
## [imports]

print( cv.__version__ )

img = cv.imread(cv.samples.findFile("media/starry_night.jpg"))

if img is None:
    sys.exit("Could not read the image.")

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("media/starry_night.png", img)