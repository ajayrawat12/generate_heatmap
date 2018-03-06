import pickle
# from datetime import datetime
# from datetime import timedelta
from generate_heatmap.process import cv_size
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def pkl_to_img(base_img_url, pickle_loc, pickle_name):
    """Add all requested heatmaps and saves it in temp.png.

    Args:
        base_img_url: base image location.
        pickle_loc: location of the pickle file.

    Returns:
        none
    """

    im_h, im_w = cv_size(base_img_url)
    print(im_h, im_w, 'from Heatmap image size')
    heat = np.zeros((im_h, im_w))

    with open(os.path.join('{}/{}.pkl'.format(pickle_loc, pickle_name)), 'rb') as f:
        heat += pickle.load(f)

    plt.imsave("{}.png".format(pickle_loc), heat, format="png", cmap="magma")
