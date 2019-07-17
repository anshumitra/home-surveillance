# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2
 
num=0

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())
 
# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
	camera = cv2.VideoCapture(0)
	time.sleep(0.25)
 
# otherwise, we are reading from a video file
else:
	camera = cv2.VideoCapture(args["video"])
 
# initialize the first frame in the video stream
firstFrame=None


# loop over the frames of the video
while True:
	time.sleep(1)
	# grab the current frame and initialize the occupied/unoccupied
	# text
	(grabbed, frame1) = camera.read()
	text = "Unoccupied"
 
	# if the frame could not be grabbed, then we have reached the end
	# of the video
	if not grabbed:
		break
 
	# first frame
	frame1 = imutils.resize(frame1, width=500)
	gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
	gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

	# secind frame after 0.01 seconds 
    time.sleep(0.01)
    (grabbed, frame2) = camera.read()
	frame2 = imutils.resize(frame2, width=500)
	gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
	gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

	# compute the absolute difference between the current frame and frist frame
	cv2.imshow('frame1', gray1)
	cv2.imshow('frame2', gray2)
	frameDelta = cv2.absdiff(gray1, gray2)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
 
	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
 
	# loop over the contours
	for c in cnts:

		# if the contour is too small, ignore it
		if cv2.contourArea(c) < args["min_area"]:
			continue
 
		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cv2.imwrite("/home/pi/Desktop/Webcame_pics/image%s.jpg" %num, frame2)
		num=num+1
		text = "Occupied"

# draw the text and timestamp on the frame
	cv2.putText(frame2, "Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame2, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame2.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
 
	# show the frame and record if the user presses a key
	cv2.imshow("Security Feed", frame2)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("Frame Delta", frameDelta)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key is pressed, break from the lop
	if key == ord("q"):
		break
 
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
