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
    '--objdir', help='Frames to skip per second', type=int,
    default=10, dest='PICKLELOC')


parser.add_argument(
    '--base_url', help='Frames to skip per second', type=int,
    default=10, dest='BASEURL')

args = parser.parse_args()

if __name__ == '__main__':
    print(args)
