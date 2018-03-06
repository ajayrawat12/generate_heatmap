# from . import joke
from generate_heatmap import config
from generate_heatmap.generate import generate_images
from generate_heatmap.process import process_image
from generate_heatmap.heatmap import pkl_to_img

VLOC = config.args.VLOC
IMGLOC = config.args.IMGLOC
SKIP = config.args.SKIP
PICKLELOC = config.args.PICKLELOC
BASEURL = config.args.BASEURL
REQDATA = config.args.REQDATA


def main():
    # print joke()
    print("Calling Generate Images")
    generate_images(VLOC, IMGLOC, SKIP)
    print("Generate pickle started...")
    process_image(IMGLOC, PICKLELOC, BASEURL, REQDATA)
    print("completed pickle...")
    pkl_to_img(base_img_url=BASEURL, pickle_loc=PICKLELOC,
               pickle_name='AjayMilGrnd-2018-03-06-16-usage')
