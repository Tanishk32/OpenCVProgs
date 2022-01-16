import numpy as np
import cv2
import os

fn = 'Example_video.avi'
set_fps = 20.0
set_res = '720p'

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

STD_DIMENSIONS = {
    "480p": {640, 480},
    "720p": {1280, 720},
    "1080p": {1920, 1080},
    "4k": {3840, 2160},
}

def get_dims(cap, res='720p'):
    width, height = STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    fn, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


cap = cv2.VideoCapture(0)
dims = get_dims(cap, set_res)
video_type_cv2 = get_video_type(fn)
output = cv2.VideoWriter(fn, video_type_cv2, set_fps, dims)


while True:
    ret, frame = cap.read()
    output.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('z'):
        break

cap.release()
output.release()
cv2.destroyAllWindows()