# Usage

## AMST2

- [AMST2](https://github.com/jhennies/AMST2) is an python alignment tool developped by Julian Hennies and wrapped up as a snakemake pipeline.
- AMST2 was installed within a conda environment according to [those guidelines](https://github.com/jhennies/AMST2?tab=readme-ov-file#installation)
- AMST2 was used within a slurm job using the following scripts and yaml files (ajouter le path) with the following cli:
  ```bash
  #launch the prealignment
  sbatch amst2_prealign.slurm
  #launch the amst part
  sbatch amst2_amst.slurm
  ```
  
- AMST2 consists of four parts: conversion to OME-Zarr, prealignment, AMST, conversion to tif
- Dataset without fiducial were aligned using AMST2
- It is also possible to just apply AMST on dataset aligned with another tool after converting it to OME-Zarr


## Taturtle (WPI)

- Taturtle is python tool to align EM data based on fiducials using template matching and applying thickness correction
- Taturtle can be run on Windows computer but was mainly run on cluster, installed as a conda env
```bash
# How to install (WPI)
git clone (ajouter le repo)
conda env create -f environment_taturtle.yaml
#on WSL
conda activate taturtle
./run_taturtle.sh
#on cluster ( à ajouter)

```
- A nextflow version of taturtle is in development

##  Squirrel 

- [Squirrel](https://github.com/jhennies/squirrel) is a Python-based library for conversion and processing of 3D EM data that is used within AMST2
- Squirrel was installed as a conda env on a WSL according to [following guidelines](https://github.com/jhennies/squirrel)
- Squirrel was used to evaluate the displacement error using the following script.( ajouter le script)
```bash
python test_val.py
```
- A nextflow version of squirrel is in development
