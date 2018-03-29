import cv2
import os
# import subprocess
# import skvideo.io


def _mov_process(vid, imgloc):
    # generate a mp4 video for now from the ffmpeg command
    # subprocess.call(['ffmpeg', '-i', vid, '-f' ,'image2', "{}/v_%05d.png".format(imgloc)])
    pass


def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (11, 11))
    return img


def generate_images(vloc, imgloc, cwd=None, skp=None):
    i = 0
    for videos in sorted([x for x in os.listdir(vloc) if not x.startswith('.')],
                         key=lambda x: x.lower()):
        print("Processing Video {}".format(videos))

        filename, file_extension = os.path.splitext(vloc)

        if file_extension[1:] in ["mov"]:
            print("Please convert the mov file into mp4 using ffmpeg or video converter.")
            return

        vid = cv2.VideoCapture('{}/{}'.format(vloc, videos))
        print(vid, 'Images for video.: ', videos)
        # i = 0
        skip = skp if skp else 10
        print("Video Processing")
        while True:
            i += 1
            grabbed, t1 = vid.read()
            if not grabbed:
                break
            if i % skip:
                continue
            t1 = preprocess(t1)
            print(i)
            cv2.imwrite('{}/{}.png'.format(imgloc, i), t1)

        vid.release()
