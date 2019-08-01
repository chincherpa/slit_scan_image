import os
from moviepy.editor import VideoFileClip
import numpy as np

from PIL import Image

basepath = r"A:"
file = 'video.mp4'

clip = VideoFileClip(os.path.join(basepath, file))

print(f'{file} is {clip.fps} fps, for {clip.duration} seconds at {clip.size}')
print('clip.size[1]', clip.size[1], 'clip.size[0]', clip.size[0])
# np.zeros is how we generate an empty ndarray
img = np.zeros((clip.size[1], clip.size[0], 3), dtype='uint8')

currentX = 0
slitwidth = 1

slitpoint = clip.size[0] // 2

# generate our target fps with width / duration
target_fps = clip.size[0] / clip.duration

for i in clip.iter_frames(fps=target_fps, dtype='uint8'):
    if currentX < (clip.size[0] - slitwidth):
        img[:, currentX:currentX + slitwidth, :] = i[:, slitpoint:slitpoint+slitwidth, :]
    currentX += slitwidth

output = Image.fromarray(img)
output.save(os.path.join(r'A:', file.split('.')[0] + '.png'))
