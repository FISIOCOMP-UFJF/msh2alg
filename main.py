import argparse
import meshio
import os
from generate_fiber_3D_biv import *

def convert_msh_to_xml(meshname):
    # Command to run dolfin-convert and convert the .msh mesh to .xml
    command = f"dolfin-convert {meshname}.msh {meshname}.xml"
    os.system(command)
    
    print(f"Mesh {meshname}.msh successfully converted to {meshname}.xml.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', type=str, default='mesh.msh', help='File with heart meshes')
    args = parser.parse_args()
    meshname = args.m

    #convert_msh_to_xml(meshname)
    #request_functions(meshname)

    os.chdir('hexa-mesh-from-VTK/')
    os.system(f'./bin/HexaMeshFromVTK -i "./{meshname}.vtu" --dx 0.5 --dy 0.5 --dz 0.5 -r 1000 -c ./conf.ini -o "./{meshname}.alg"')
    os.chdir('../')


if __name__ == "__main__":
    main()