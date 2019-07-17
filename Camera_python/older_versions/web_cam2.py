# does not work, error on VIDIOC_S_FMT unsupported format

import pygame, sys
import pygame.camera
from pygame.locals import *


pygame.init()
pygame.camera.init()
camera = pygame.camera.Camera("/dev/video0", (384,288))
camera.start()
image = camera.get_image()
pygame.image.save(image, 'image.jpg')
camera.stop()
    
