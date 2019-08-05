import os
import sys
import numpy as np
import cv2

this_path = os.path.dirname(os.path.realpath(__file__))
filename = 'big_buck_bunny_720p_5mb.mp4'
path_to_file = os.path.join(this_path, filename)
output_filename = os.path.splitext(os.path.basename(path_to_file))[0] + '.png'

clip = cv2.VideoCapture(path_to_file)
first_frame = clip.read()
height, width, dpth = first_frame[1].shape

slitwidth = 1
slitpoint = width // 2

# np.zeros is how we generate an empty ndarray
img = np.zeros((height, 1, dpth), dtype='uint8')

while True:
    frame = clip.read()
    if frame[0] is False:
        break

    frame = np.array(frame[1])

    slit = frame[:,slitpoint:slitpoint+slitwidth,:]
    img = np.hstack((img, slit))

    cv2.imshow("Frames", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

output = cv2.imwrite(os.path.join(this_path, output_filename), img)
clip.release()
