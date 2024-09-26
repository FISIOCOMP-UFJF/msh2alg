import argparse
import os
from generate_fiber_3D_biv import *

def convert_msh_to_xml(pathMesh, meshname):
    # Command to run dolfin-convert and convert the .msh mesh to .xml
    command = f"dolfin-convert {pathMesh} {meshname}.xml"
    os.system(command)
    
    print(f"Mesh successfully converted to {meshname}.xml.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, default='', help='Path to file with heart meshes')
    parser.add_argument('-o', type=str, default='patient', help='Name output file')
    parser.add_argument('-dx', type=float, default=0.5, help='dx')
    parser.add_argument('-dy', type=float, default=0.5, help='dy')
    parser.add_argument('-dz', type=float, default=0.5, help='dz')
    args = parser.parse_args()
    pathMesh = args.i
    meshname = args.o

    convert_msh_to_xml(pathMesh, meshname)
    request_functions(meshname)
    
    print("================================================================================")
    print("Converting to alg...")
    os.chdir('hexa-mesh-from-VTK/')
    os.system(f'./bin/HexaMeshFromVTK -i "../{meshname}.vtu" --dx {args.dx} --dy {args.dy} --dz {args.dz} -r 1000 -c ../conf.ini -o "./{meshname}.alg"')
    os.chdir('../')


if __name__ == "__main__":
    main()