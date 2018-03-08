import pickle
# from datetime import datetime
# from datetime import timedelta
import pycurl
from generate_heatmap.process import cv_size
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def pkl_to_img(base_img_url, pickle_loc, pickle_name, heat_loc, p_code=None, h_code=None, api=None):
    """Add all requested heatmaps and saves it in temp.png.

    Args:
        base_img_url: base image location.
        pickle_loc: location of the pickle file.
        pickle_name: name of the pickle file.
        heat_loc: location of the heatmap to be saved.

    Returns:
        none
    """

    im_h, im_w = cv_size(img=base_img_url)
    heat = np.zeros((im_h, im_w))

    with open(os.path.join('{}/{}.pkl'.format(pickle_loc, pickle_name)), 'rb') as f:
        heat += pickle.load(f)

    plt.imsave("{}/{}.png".format(heat_loc, pickle_name), heat, format="png", cmap="magma")
    img_url = "{}/{}.png".format(heat_loc, pickle_name)
    if (p_code and h_code and api):
        # Send the Data to api
        resp = send_heatmap(img_url, p_code, h_code, api)
        print(resp)


def send_heatmap(img_url, p_code, h_code, api):
    try:
        headers = {'Authorization': p_code}
        data = {
            'h_code': h_code
        }
        reqobj = pycurl.post(api, json=data, headers=headers)
        print('Data Sent to the API')
    except Exception as e:
        raise e
