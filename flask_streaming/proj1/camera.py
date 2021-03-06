# https://pythonpedia.com/en/knowledge-base/49939859/flask-video-stream-using-opencv-images


# camera.py
import cv2


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        #####self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        self.video = cv2.VideoCapture('video.mp4')
        # ret, frame = self.video.read()
        # print(frame)
        # print("==========================video captured=================================")

    def __del__(self):
        self.video.release()

    def get_frame(self):
        print("==========================In get frames=================================")
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        # cv2.imshow('win1',image)
        # cv2.waitKey(0)
        return jpeg
