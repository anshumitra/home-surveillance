# Home surveillance system using Raspberry Pi

## Objective
1. Scan camera images to detect motion.  
2. Send information to remote owner.  
3. Create speech (from owner’s text message) to warn the intruder. 

## Tools Used
* Raspberry Pi 3
* Webcam
* OpenCV
* TTS (Text2Speech)
* IBM Bluemix

## Description

Using [OpenCV](http://opencv.org), the difference between consecutive images is computed to detect motion in the vicinity. If such a motion is detected, an email is sent to the owner with a snapshot of the intruder. The owner can send a text message through [IBM Bluemix](https://www.ibm.com/cloud-computing/bluemix), which is converted to speech through [TTS](http://www.cstr.ed.ac.uk/projects/festival), and is played through RPi’s speaker to
warn or communicate with the intruder.
