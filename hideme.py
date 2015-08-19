"""
Created By: Phillip Ochola
Email: its2uraps@msn.com
GitHandle: github.com/its2mc
License: ISC

This code forms the base for the worm that I am researching. The worm 
is meant to discretely filter out faces from a ip camera stream in a security
system. This algorithm takes an mp4 file called a in folder 'original' and
then processes it... blurres out any faces detected in each frame then 
writes the output into an avi file. My machine did not have the codec to 
support mp4.. i have to install it i think so for now we will settle on the avi encoding

"""

#import libraries
import cv2
import cv2.cv as cv
import time
import numpy as np

#specify the cascadeclassifier files for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#We get initial properties of the video 
cap = cv2.VideoCapture('original/a.mp4')
ret, f_img = cap.read()

#Get the size of the video
size = f_img.shape
width = size[0]
height = size[1]

#Get the fps of the video
fps = cap.get(cv.CV_CAP_PROP_FPS)

#Set the blurring filter kernel (an averaging matrix for the image matrix)
kernel =  np.ones((50,50),np.float32)/2500

#Describe the output stream
output = cv2.VideoWriter('edited/a_out.avi',-1, fps, (height,width))

print("Hiding your a**")

while True:
	#Read from the image and store in a mat
	ret, img = cap.read()
	mat = np.asarray(img[:,:])

	#Do face detection on a grayscale image.. for speed
	gray = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		#Get the image roi.. and filter with the blurring kernel then overwrite the original
		roi_color = mat[y:y+h, x:x+w]
		filtered = cv2.filter2D(roi_color,-1,kernel)
		mat[y:y+h, x:x+w] = filtered

	#Write out to the image.
	output.write(mat)
	if cv.WaitKey(10) == 27:
		break