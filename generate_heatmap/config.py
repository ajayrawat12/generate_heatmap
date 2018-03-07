# import os
import argparse
from pathlib import Path


USERHOME = str(Path.home())


parser = argparse.ArgumentParser(
    description='Generate the heatmaps from a video',
    epilog='Be patient for some more help!!!')

parser.add_argument(
    '--vloc', help='Full Location of the video in your system.',
    default=USERHOME, type=str, dest='VLOC')

parser.add_argument(
    '--imgloc', help='Location where images generated from the video will be stored.',
    default=USERHOME, type=str, dest='IMGLOC')

parser.add_argument(
    '--skp', help='Frames to skip per second', type=int,
    default=10, dest='SKIP')

parser.add_argument(
    '--pickleloc', help='Location of the pickle file', type=str,
    default=USERHOME, dest='PICKLELOC')


parser.add_argument(
    '--baseurl', help='Base Image URL of the Camera', type=str, dest='BASEURL')

parser.add_argument(
    '--reqdata', help='Camera and Request Details in the Request', type=str, dest='REQDATA')

parser.add_argument(
    '--heatloc', help='Location of the heatmap to be stored', type=str, dest='HEATLOC')

args = parser.parse_args()

if __name__ == '__main__':
    print(args)
