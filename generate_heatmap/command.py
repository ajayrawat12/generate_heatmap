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
HEATLOC = config.args.HEATLOC


def main():
    # print joke()
    # print("Calling Generate Images")
    # generate_images(VLOC, IMGLOC, SKIP)
    print("Generate pickle started...this might take upto 10-15 mins to complete.")
    process_image(IMGLOC, PICKLELOC, BASEURL, REQDATA)
    print("completed pickle...Pickle to image started")
    pkl_to_img(base_img_url=BASEURL, pickle_loc=PICKLELOC,
               pickle_name=REQDATA, heat_loc=HEATLOC)
    print('completed image from pickle....')


# --imgloc /Users/ajayrawat/cowrks/videos_data/mill_img --pickleloc /Users/ajayrawat/cowrks/videos_data/milPickle --reqdata millGrndHeat --baseurl /Users/ajayrawat/cowrks/videos_data/mill_img/15.png