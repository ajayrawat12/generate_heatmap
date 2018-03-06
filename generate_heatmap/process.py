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


def process_image(img_dir, out_dir, base_img_url):
    imgs = os.listdir(img_dir)
    imgs.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    # imgs.sort()

    base_img_url = base_img_url if base_img_url else imgs[0]
    no_motion = cv2.imread(base_img_url, 0)
    # 0 in the end is for black and white

    usage = np.zeros((1080, 1920))

    for img_loc in imgs[1:]:
        # print(img_loc)
        img = cv2.imread('{}/{}'.format(img_dir, img_loc), 0)
        usage += cv2.absdiff(no_motion, img)

    last_hour = (datetime.now() - timedelta(hours=1)).isoformat('-', 'hours')
    print(usage.max(), usage.min())

    with open(os.path.join(out_dir, '{}-usage.pkl'.format(last_hour)), 'wb+') as f:
        pickle.dump(process_map(usage), f)
