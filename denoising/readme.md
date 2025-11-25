# Usage

## Installation

- [CAREamics](https://careamics.github.io/0.1/) is a PyTorch library aimed at simplifying the use of state of the art image restoration deep-learning algorithms, such as CARE, Noise2Void, HDN, MicroSplit, etc.
- This librairy is developped by the Human technopole italy, led by Florian Hug (à vérifier)
- Careamics can be installed as a conda or uv environment following [those guidelines](https://careamics.github.io/0.1/installation/)
- For sustainable usage, we have containerize careamics as an apptainer and a docker image
```bash
# cli to build the docker image
docker build -tag careamics:latest .
# cli to build the apptainer image
apptainer build careamics.sif careamics.def
```
- nota bene to use careamics within nextflow, the newest version of careamics docker and container image are available at [seqera containers](https://seqera.io/containers/)

## How to use
- careamics was used as a python script from a container on Tier1 and Tier2 cluster at the [Flemish supercomputer center](https://www.vscentrum.be/) and we used the model n2v2 to denoise the data
```bash
# running the training
sbatch training_careamics.slurm
# running the prediction once the training job has succeded
sbatch -d afterok:jobid_training_careamics predict_careamics.slurm
```
## Documentation and future prospects
- nextflow and nfcore modules for careamics are in development
- [API documentation for careamics]()
- [current application for careamics](https://careamics.github.io/0.1/applications/)
