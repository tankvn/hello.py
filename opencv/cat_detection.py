## [imports]
import cv2
## [imports]

image = cv2.imread('media/black-cat.jpg') # must pass valid file directory

# Initializing the haar cascade
cat_cascade = cv2.CascadeClassifier("data/haarcascade_frontalcatface.xml")
# cat_cascade = cv2.CascadeClassifier("data/haarcascade_frontalcatface_extended.xml")

cat_faces = cat_cascade.detectMultiScale(image)

for (x,y,w,h) in cat_faces:
    cv2.rectangle(image,(x ,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(image,'Cat Detected',(x,y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2, cv2.LINE_AA)   

cv2.imshow("ImageWindow", image) # displaying the image
cv2.waitKey(0) #waitKey is set to 0, that means the image window will close as soon as any key is pressed.
cv2.destroyAllWindows()