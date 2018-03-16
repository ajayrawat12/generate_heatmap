import os
import argparse
from pathlib import Path

CWD = os.getcwd()
USERHOME = str(Path.home())

"""
To create dir in CWD if DIR is not provided.
pathlib.Path('/{}/IMGS'.format(CWD)).mkdir(parents=True, exist_ok=True)
"""

parser = argparse.ArgumentParser(
    description='Generate the heatmaps from a video',
    epilog='Be patient for some more help!!!')

parser.add_argument('-v', '--vloc', help='Location of the video, Default:Current Dir.',
                    default=CWD, type=str, dest='VLOC')

parser.add_argument('-i', '--imgloc', help='Images generated from video stored.',
                    default=USERHOME, type=str, dest='IMGLOC')

parser.add_argument('-s', '--skp', help='Frames to skip per second',
                    type=int, default=22, dest='SKIP')

parser.add_argument('-p', '--pickleloc', help='Location of the pickle file, Default:Current Dir.',
                    type=str, default=CWD, dest='PICKLELOC')


parser.add_argument('-b', '--baseurl', help='Base Image URL of the Camera',
                    type=str, dest='BASEURL')

parser.add_argument('-r', '--reqdata', help='Camera and Request Details in the Request',
                    type=str, dest='REQDATA')

parser.add_argument('-hl', '--heatloc', help='Location of the heatmap to be stored',
                    type=str, dest='HEATLOC')

# Non Mandatory Parameters.
parser.add_argument('-pass', '--password', action='store',
                    help='Password for authentication', dest='PASSWORD')

parser.add_argument('-hc', '--heatcode', action='store',
                    help='heatmap code', dest='HEATCODE')

parser.add_argument('-u', '--apiurl',
                    help='API URL to send data', type=str, dest='APIURL')

args = parser.parse_args()

if __name__ == '__main__':
    print(args)
