#!/bin/bash
#SBATCH --job-name=amst2_prealign
#SBATCH -A 
#SBATCH --partition=
#SBATCH --nodes="1"
#SBATCH --ntasks-per-node="1"
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=1G
#SBATCH --output=amst2_prealigned.out
#SBATCH --error=amst2_prealigned.err
#SBATCH --time=02:00:00

source activate amst2-env
amst2-wf-nsbs_pre_align-run $VSC_SCRATCH/dataset_to_align/params_pre_align.yaml
