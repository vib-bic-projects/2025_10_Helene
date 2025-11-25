#!/bin/bash
#SBATCH --job-name=amst2_amst
#SBATCH -A 
#SBATCH --partition=
#SBATCH --nodes="1"
#SBATCH --ntasks-per-node="1"
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=1G
#SBATCH --output=amst2_amst.out
#SBATCH --error=amst2_amst.err
#SBATCH --time=02:00:00

source activate amst2-env
amst2-wf-amst-run $VSC_SCRATCH/dataset_to_align/params_amst.yaml
