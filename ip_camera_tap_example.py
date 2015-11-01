import cv2
import time

capture = cv2.VideoCapture("http://www.andaluz.tv/webcams/calvo/current.jpg")

#while (1):
ret,frame = capture.read()
while(1):
	cv2.imshow('camera', frame)
	if cv2.waitKey(10) == 27:
		break
#cv2.DestroyAllWindows()