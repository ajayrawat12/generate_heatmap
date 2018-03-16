import pickle
import os
import json
import base64
import requests
from generate_heatmap.process import cv_size
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def pkl_to_img(base_img_url, pickle_loc, pickle_name, heat_loc, p_code=None, h_code=None, api=None):
    """ Read the pickle file and convert it into heatmap image.
        Save the Requested heatmap.

    Args:
        base_img_url: base image location.
        pickle_loc: location of the pickle file.
        pickle_name: name of the pickle file.
        heat_loc: location of the heatmap to be saved.

    Returns:
        none
    """

    print(pickle_loc, pickle_name)

    im_h, im_w = cv_size(img=base_img_url)
    heat = np.zeros((im_h, im_w))

    with open(os.path.join('{}/{}.pkl'.format(pickle_loc, pickle_name)), 'rb') as f:
        heat += pickle.load(f)

    img_name = "{}.png".format(pickle_name)
    img_url = "{}/{}".format(heat_loc, img_name)

    plt.imsave("{}".format(img_url), heat, format="png", cmap="magma")
    print('image heatmap generate completed.')

    if (p_code and h_code and api):
        # Send the Data to api
        send_heatmap(img_url, img_name, p_code, h_code, api)


def send_heatmap(img_url, img_name, p_code, h_code, API):
    try:
        # Sending image file as base64 encoded format.
        # ToDo: can reduce the image file and then send to API.
        with open(img_url, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        payload = {'filename': img_name,
                   'h_code': h_code,
                   'p_code': p_code,
                   'fileupload': json.dumps(encoded_string.decode("utf-8")),
                   }

        resp = requests.put(API, json=payload)
        print('Data sent to the API...', resp)
        json_data = json.loads(resp.text)
        print('Message From API..', json_data['message'])
    except Exception as e:
        print(str(e))
