# from . import joke
from generate_heatmap import config
from generate_heatmap.generate import generate_images
from generate_heatmap.process import process_image

VLOC = config.args.VLOC
IMGLOC = config.args.IMGLOC
SKIP = config.args.SKIP
PICKLELOC = config.args.PICKLELOC
BASEURL = config.args.BASEURL


def main():
    # print joke()
    print("Calling Generate Images")
    generate_images(VLOC, IMGLOC, SKIP)
    print("Generate Images call completed...")
    process_image(IMGLOC, PICKLELOC, BASEURL)
