import cv2
# ToDo : Need to test on Windows Machine


def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (11, 11))
    return img


def generate_images(vloc, imgloc, skp=None):
    vid = cv2.VideoCapture(vloc)

    i = 0
    skip = skp if skp else 10
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
