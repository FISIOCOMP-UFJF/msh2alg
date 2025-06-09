# msh2alg

## Pre-Requisites
All dependencies are already included in the provided Conda environment:

- FEniCS 2019.1.0
- Gmsh
- LDRB
- meshio
- h5py 
- scipy
- CMake
- VTK (>= 9.0)
- [hexa-mesh-from-VTK](https://github.com/FilipeNamorato/hexa-mesh-from-VTK_vtk9.git): This repository is necessary for the generation of hexahedral meshes from VTK files.

## Environment Setup

### 1. Create Conda environment

```sh
conda env create -f environment.yml
```

### 2. Activate environment

```sh
conda activate myomesh
```

## Configuration
```sh
bash config.sh
```

## Description of parameters

- `-i`: Path to the input `.msh` file (heart mesh).
- `-o`: Name for the output folder.
- `-dx`, `-dy`, `-dz`: Discretization spacing for the `.vtu`. Recommended value is `0.5`.
- `--alpha_endo_lv`: Fiber angle on the left ventricle (LV) endocardium. Default: `30°`.
- `--alpha_epi_lv`: Fiber angle on the left ventricle (LV) epicardium. Default: `-30°`.
- `--beta_endo_lv`: Sheet angle on the left ventricle (LV) endocardium. Default: `0°`.
- `--beta_epi_lv`: Sheet angle on the left ventricle (LV) epicardium. Default: `0°`.
- `--alpha_endo_sept`: Fiber angle on the septum endocardium. Default: `60°`.
- `--alpha_epi_sept`: Fiber angle on the septum epicardium. Default: `-60°`.
- `--beta_endo_sept`: Sheet angle on the septum endocardium. Default: `0°`.
- `--beta_epi_sept`: Sheet angle on the septum epicardium. Default: `0°`.
- `--alpha_endo_rv`: Fiber angle on the right ventricle (RV) endocardium. Default: `80°`.
- `--alpha_epi_rv`: Fiber angle on the right ventricle (RV) epicardium. Default: `-80°`.
- `--beta_endo_rv`: Sheet angle on the right ventricle (RV) endocardium. Default: `0°`.
- `--beta_epi_rv`: Sheet angle on the right ventricle (RV) epicardium. Default: `0°`.

## Running the pipeline

```sh
python3 main.py -i path_to_mesh.msh -o output_folder -dx 0.5 -dy 0.5 -dz 0.5
```

## Running example (default fiber parameters)

```sh
python3 main.py -i ./patient1.msh -o output -dx 0.5 -dy 0.5 -dz 0.5
```

## Running example (custom fiber parameters)

```sh
python3 main.py -i ./patient1.msh -o output -dx 0.5 -dy 0.5 -dz 0.5 \
--alpha_endo_lv 30 --alpha_epi_lv -30 --beta_endo_lv 0 --beta_epi_lv 0 \
--alpha_endo_sept 60 --alpha_epi_sept -60 --beta_endo_sept 0 --beta_epi_sept 0 \
--alpha_endo_rv 80 --alpha_epi_rv -80 --beta_endo_rv 0 --beta_epi_rv 0
```
