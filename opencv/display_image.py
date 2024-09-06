## [imports]
import cv2 as cv
import sys
## [imports]

print( cv.__version__ )

img = cv.imread(cv.samples.findFile("data/starry_night.jpg"))
 
if img is None:
    sys.exit("Could not read the image.")
    
cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("starry_night.png", img)