import cv2
import os
# ToDo : Need to test on Windows Machine


def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (11, 11))
    return img


def generate_images(vloc, imgloc, skp=None):
    i = 0
    for videos in sorted([x for x in os.listdir(vloc) if not x.startswith('.')],
                         key=lambda x: x.lower()):

        vid = cv2.VideoCapture('{}/{}'.format(vloc, videos))
        print(vid, 'Images for video.: ', videos)
        # i = 0
        skip = 15
        # print("skip is", skip)
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
