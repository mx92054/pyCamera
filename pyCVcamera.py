# -*- coding: UTF-8
# created by chenming

import cv2
import time

#url = 'rtsp://192.168.1.64/media/video1'  #SONY camera
url = 'rtsp://admin:sidsse401@10.3.41.236:554//Streaming/Channels/1'  #HIKIVISION camera

i = 0
cap = cv2.VideoCapture(url)

font = cv2.FONT_HERSHEY_SIMPLEX

t1 = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    t2 = time.time()

    tval = int(1/(t2 - t1))
    t1 = t2

    (h, w) = frame.shape[:2]
    newframe = cv2.resize(frame, (1920, 1080), interpolation=cv2.INTER_AREA)

    localtime = time.asctime(time.localtime(time.time()))
    cv2.putText(newframe, localtime, (5, 40), font, 0.5, (255, 255, 255), 1)
    cv2.putText(newframe, 'fps: ' + str(tval), (5, 60), font, 0.5, (255, 255, 255), 1)

    cv2.imshow('HikiVision Capture', newframe)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('w'):
        i += 1
        imgName = 'img_' + str(i)
        cv2.imwrite('.//img//' + imgName + '.jpg', frame)

cap.release()
cv2.destroyAllWindows()

#end of file

