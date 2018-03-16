from datetime import datetime
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
PASSWORD = config.args.PASSWORD
HEATCODE = config.args.HEATCODE
APIURL = config.args.APIURL


def main():
    print(config.CWD)
    st = datetime.now()
    print("Imgs from vid., can take upto 15-20 mins, for 3-4 videos in folder.")
    generate_images(VLOC, IMGLOC, SKIP)
    et_vid = datetime.now()

    print("Images generation completed in {}.".format((et_vid - st)))
    print("Generate pickle started...this might take upto 10-15 mins to complete.")

    process_image(IMGLOC, PICKLELOC, BASEURL, REQDATA)
    et_pick = datetime.now()

    print("completed pickle generation from video in {} .".format(et_pick - et_vid))
    print("starting Heatmap from images")

    pkl_to_img(base_img_url=BASEURL, pickle_loc=PICKLELOC,
               pickle_name=REQDATA, heat_loc=HEATLOC, p_code=PASSWORD, h_code=HEATCODE,
               api=APIURL)

    print('Completed... heatmap image.')

    et = datetime.now()
    print("completed processing in {} .".format(et - st))
