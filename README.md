# msh2alg

## Pre-Requisites
FEniCS 2019.1.0
Gmsh
meshio
h5py
Scipy
CMake
VTK (libvtk7-dev)
hexa-mesh-from-VTK: This repository is necessary for the generation of hexahedral meshes from VTK files. It will be cloned during the Configuration.

## Configuration
  ```sh
    bash config.sh
  ```

## Description parameters
- i: Path to file with heart meshes
- o: Name to output file
- dx, dy, and dz: refer to the discretization for the .vtu. Conventionally, we use the value of 0.5.

## Running
```sh
conda activate fenicsproject
```
```sh
python3 -i path_mesh -o output_file_name -dx dx -dy dy -dz dz
```
## Running example
```sh
python3 main.py -i ./patient1.msh -o output -dx 0.5 -dy 0.5 -dz 0.5
``` 