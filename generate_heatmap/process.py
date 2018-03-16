import cv2
import numpy as np
import os
import pickle


def process_map(heatmap):
    """Post-processing on the heatmap.

    Args:
        heatmap (1080, 1920)

    Returns:
        processed heatmap

    # Remove movement of timer on top right
    # row, col = np.indices((55, 595))
    # heatmap[row + 40, col + 1265] = 0

    # Remove last 1/15 of the motion

    About CV2:

        cv2.threshold(),
        First argument is the source image, which should be a grayscale image.
        Second argument is the threshold value which is used to classify the pixel values.
        Third argument is the maxVal which represents the value to be given,
        If pixel value is more than (sometimes less than) the threshold value.
        OpenCV provides different styles of thresholding, it is decided by fourth parameter.
        Different types are:
        cv.THRESH_BINARY
        cv.THRESH_BINARY_INV
        cv.THRESH_TRUNC
        cv.THRESH_TOZERO
        cv.THRESH_TOZERO_INV
    """

    heatmap = cv2.threshold(heatmap, heatmap.max() / 400, 255, cv2.THRESH_TOZERO)[1]
    return heatmap


def cv_size(img, img_dir=None):
    if img_dir:
        img_data = cv2.imread('{}/{}'.format(img_dir, img))
    else:
        img_data = cv2.imread(img)
    img_size = tuple(img_data.shape[1::-1])
    return img_size[1], img_size[0]


def process_image(img_dir, out_dir, base_img_url, req_data):
    if not os.path.isdir(img_dir):
        print('IMGLOC is not a directory.')
        return False

    imgs = [x for x in os.listdir(img_dir) if not x.startswith('.')]
    imgs.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

    base_img_url = base_img_url if base_img_url else imgs[0]
    no_motion = cv2.imread(base_img_url, 0)

    im_h, im_w = cv_size(img=imgs[0], img_dir=img_dir)
    usage = np.zeros((im_h, im_w))

    for img_loc in imgs[1:]:
        img = cv2.imread('{}/{}'.format(img_dir, img_loc), 0)
        usage += cv2.absdiff(no_motion, img)

    with open(os.path.join(out_dir, '{}.pkl'.format(req_data)), 'wb+') as f:
        pickle.dump(process_map(usage), f)
