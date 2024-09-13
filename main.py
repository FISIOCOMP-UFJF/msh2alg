import argparse
from generate_fiber_3D_biv.py import *

import os
parser = argparse.ArgumentParser()
parser.add_argument('-m', type=str, default='mesh.msh', help='File with hearth meshs')

args = parser.parse_args()
meshname = args.m

request_functions(meshname)