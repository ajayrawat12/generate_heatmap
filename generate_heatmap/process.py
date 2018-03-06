import cv2
import numpy as np
import os
from datetime import datetime
from datetime import timedelta
import pickle


def process_map(heatmap):
    """Post-processing on the heatmap.

    Args:
        heatmap (1080, 1920)

    Returns:
        processed heatmap
    """
    # Remove movement of timer on top right
    # row, col = np.indices((55, 595))
    # heatmap[row + 40, col + 1265] = 0

    # Remove last 1/15 of the motion
    heatmap = cv2.threshold(heatmap, heatmap.max() / 15, 255, cv2.THRESH_TOZERO)[1]
    return heatmap


def cv_size(img):
    img_data = cv2.imread(img)
    img_size = tuple(img_data.shape[1::-1])
    return img_size[1], img_size[0]


def process_image(img_dir, out_dir, base_img_url, req_data):
    if not os.path.isdir(img_dir):
        # ToDo: need to generate error if the input is not dir.
        return False

    imgs = os.listdir(img_dir)
    imgs.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

    base_img_url = base_img_url if base_img_url else imgs[0]
    no_motion = cv2.imread(base_img_url, 0)
    # 0 in the end is for black and white

    im_h, im_w = cv_size(imgs[0])
    print(im_h, im_w)
    usage = np.zeros((im_h, im_w))

    for img_loc in imgs[1:]:
        # print(img_loc)
        img = cv2.imread('{}/{}'.format(img_dir, img_loc), 0)
        usage += cv2.absdiff(no_motion, img)

    last_hour = (datetime.now() - timedelta(hours=1)).isoformat('-', 'hours')
    print(usage.max(), usage.min())

    with open(os.path.join(out_dir, '{}-{}-usage.pkl'.format(req_data, last_hour)), 'wb+') as f:
        pickle.dump(process_map(usage), f)
