## [imports]
import cv2
import time
## [imports]

car_cascade = cv2.CascadeClassifier('data/carshaar.xml')
cap = cv2.VideoCapture('media/carsvid.wmv')
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
fps = 0  # set initial fps variable to 0

while 1:

        start_time = time.time() # note the current time at the start of the loop
        ret, image = cap.read()
        if not ret:
             break
        resized_image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)

        cars = car_cascade.detectMultiScale(resized_image)

        ratio = 1 / 0.5
        for (x,y,w,h) in cars:
                x = int(x * ratio)
                y =int( y * ratio)
                w = int(w * ratio)
                h =int( h * ratio)

                cv2.rectangle(image,(x ,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(image,'Car Detected',(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,255,0), 1, cv2.LINE_AA)
                cv2.putText(image, 'FPS: {:.2f}'.format(fps), (20, 50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),1,cv2.LINE_AA)

        cv2.imshow('img',image)

        # Minus the current time with start time to get total time for this loop
        total_time = time.time() - start_time

        # divide the no of frames (1 in this case)/ by total time it took.
        # And now you have the Fps, which you display on each frame
        fps= (1.0 / total_time)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()