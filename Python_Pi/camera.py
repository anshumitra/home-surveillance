from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

### below lines are for stil image
#camera.exposure_mode='antishake'
#sleep(5)
#camera.capture('/home/pi/Desktop/Python/image.jpg')

### below lines are for video
camera.start_recording('/home/pi/Desktop/Python/video.h264')
sleep(5)
camera.stop_recording()

camera.stop_preview()

