# import pickle
# from datetime import datetime
# from datetime import timedelta
import base64
import pycurl
from generate_heatmap.process import cv_size
import numpy as np
# import os
import matplotlib
matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# from urllib.parse import urlencode


def pkl_to_img(base_img_url, pickle_loc, pickle_name, heat_loc, p_code=None, h_code=None, api=None):
    """Save the Requested heatmap.

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

    # with open(os.path.join('{}/{}.pkl'.format(pickle_loc, pickle_name)), 'rb') as f:
    #     heat += pickle.load(f)

    # plt.imsave("{}/{}.png".format(heat_loc, pickle_name), heat, format="png", cmap="magma")
    img_name = "{}.png".format(pickle_name)
    img_url = "{}/{}".format(heat_loc, img_name)
    if (p_code and h_code and api):
        # Send the Data to api
        resp = send_heatmap(img_url, img_name, p_code, h_code, api)
        print(resp)


def send_heatmap(img_url, img_name, p_code, h_code, API):
    try:
        with open(img_url, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        # print(img_url, post_data, 'Data img URL and Post Data.')

        c = pycurl.Curl()
        # c.setopt(c.CONNECTTIMEOUT, 5)
        c.setopt(c.POST, 1)
        c.setopt(c.URL, API)
        c.setopt(c.HTTPPOST, [('fileupload', (encoded_string)),
                              ('filename', img_name),
                              ('h_code', h_code)])
        # c.setopt(c.HTTPPOST, [('h_code', h_code)])
        # c.setopt(c.POSTFIELDS, post_data)
        c.setopt(pycurl.CUSTOMREQUEST, "PUT")
        c.perform()
        c.close()

        # headers = {'Authorization': p_code}
        print('Data sent')
    except Exception as e:
        raise e
