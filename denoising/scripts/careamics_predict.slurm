#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --partition=    
#SBATCH --time=00:25:00
#SBATCH --job-name=careamics_predict
#SBATCH --output=careamics_predict.out
#SBATCH --error=careamics_predict.err
#SBATCH --cpus-per-task=4
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1
#SBATCH --mem-per-cpu=4G
#SBATCH -A 

APPTAINER_CACHEDIR=$VSC_SCRATCH/.apptainer/cache
APPTAINER_TMPDIR=$VSC_SCRATCH/.apptainer/tmp
apptainer run --nv  careamics.sif python  careamics_predict.py
