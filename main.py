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

    parser.add_argument('--alpha_endo_lv', type=float, default=30, help='Fiber angle on the LV endocardium')
    parser.add_argument('--alpha_epi_lv', type=float, default=-30, help='Fiber angle on the LV epicardium')
    parser.add_argument('--beta_endo_lv', type=float, default=0, help='Sheet angle on the LV endocardium')
    parser.add_argument('--beta_epi_lv', type=float, default=0, help='Sheet angle on the LV epicardium')

    parser.add_argument('--alpha_endo_sept', type=float, default=60, help='Fiber angle on the Septum endocardium')
    parser.add_argument('--alpha_epi_sept', type=float, default=-60, help='Fiber angle on the Septum epicardium')
    parser.add_argument('--beta_endo_sept', type=float, default=0, help='Sheet angle on the Septum endocardium')
    parser.add_argument('--beta_epi_sept', type=float, default=0, help='Sheet angle on the Septum epicardium')

    parser.add_argument('--alpha_endo_rv', type=float, default=80, help='Fiber angle on the RV endocardium')
    parser.add_argument('--alpha_epi_rv', type=float, default=-80, help='Fiber angle on the RV epicardium')
    parser.add_argument('--beta_endo_rv', type=float, default=0, help='Sheet angle on the RV endocardium')
    parser.add_argument('--beta_epi_rv', type=float, default=0, help='Sheet angle on the RV epicardium')

    args = parser.parse_args()

    pathMesh = args.i
    meshname = args.o

    alpha_endo_lv = args.alpha_endo_lv
    alpha_epi_lv = args.alpha_epi_lv
    beta_endo_lv = args.beta_endo_lv
    beta_epi_lv = args.beta_epi_lv

    alpha_endo_sept = args.alpha_endo_sept
    alpha_epi_sept = args.alpha_epi_sept
    beta_endo_sept = args.beta_endo_sept
    beta_epi_sept = args.beta_epi_sept

    alpha_endo_rv = args.alpha_endo_rv
    alpha_epi_rv = args.alpha_epi_rv
    beta_endo_rv = args.beta_endo_rv
    beta_epi_rv = args.beta_epi_rv

    convert_msh_to_xml(pathMesh, meshname)
    request_functions(meshname, alpha_endo_lv, alpha_epi_lv, beta_endo_lv, 
                beta_epi_lv, alpha_endo_sept, alpha_epi_sept, beta_endo_sept,
                beta_epi_sept, alpha_endo_rv, alpha_epi_rv, 
                beta_endo_rv, beta_epi_rv)    
    print("================================================================================")
    print("Converting to alg...")
    os.chdir('hexa-mesh-from-VTK/')
    os.system(f'./bin/HexaMeshFromVTK -i "../{meshname}.vtu" --dx {args.dx} --dy {args.dy} --dz {args.dz} -r 1000 -c ../conf.ini -o "./{meshname}.alg"')
    os.chdir('../')


if __name__ == "__main__":
    main()