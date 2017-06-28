import numpy as np
import cv2
import time
from scipy.cluster import vq

K = 4

#Firs Step: Change frame format - RGB -> YCRCB
def convertRGBtoYCrCb(frame):
	frameYCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
	return frameYCrCb

#Second Step: Change frame format - YCRCB -> HSV
def convertYCrCbtoHSV(frame):
	frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	return frameHSV

#Take Photos
def getPhotos(camera):
	retval, im = camera.read()
	return im

def Kmeans_img(K, frame):
	z = frame.reshape((-1,3))

	center, dist 	= vq.kmeans(z, K)
	code, distace 	= vq.vq(z, center)
	res 		= center[code]
	res2 		= res.reshape((frame.shape))  

	return res2

def preProcess(img):
	frameYCrCb 	= convertRGBtoYCrCb(img)
	ch1, ch2, ch3 	= cv2.split(frameYCrCb)
	ch1 		= cv2.equalizeHist(ch1)

	frameYCrCb 	= cv2.merge((ch1, ch2, ch3))
	frameHSV 	= convertYCrCbtoHSV(frameYCrCb)
	imgKmeans 	= Kmeans_img(K, frameHSV)

	return imgKmeans

def openCap(cap):
	val 	= False
	maxTry 	= 100
	cTry 	= 0

	if cap.isOpened():
	    while (not val) and (cTry < maxTry):
		val, frame = cap.read()
		cTry = cTry + 1
	else:
	    return False
	
	if val:
	    return True

if __name__ == "__main__":
	#Open Webcam
	cap 		= cv2.VideoCapture(0)
	filename 	= "photos/"
	t0 		= time.time()
	print "Time: ", t0
	index 		= 1
	
	if openCap(cap):
		while (time.time() - t0) < 30:

			if (int((time.time() - t0))%10 == 0):
				img	= getPhotos(cap)
				cv2.imwrite(filename+"image_"+str(index)+".png", img)
				index += 1

	del(cap)

	print "Iniciando Pre-processamento"
	#Read all images

	index -= 1
	while index > 0:
		print index
		imgFile 	= cv2.imread(filename+"image_"+str(index)+".png", flags = cv2.IMREAD_COLOR)
		imgpreProcess 	= preProcess(imgFile)
		cv2.imwrite(filename+"image_"+str(index)+"_process"+".png", imgpreProcess)
		index -= 1

