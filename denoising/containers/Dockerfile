# Use Miniconda3 as the base image
FROM continuumio/miniconda3

# Set environment variables
ENV CONDA_BIN_PATH="/opt/conda/bin"
ENV PATH="$CONDA_BIN_PATH:$PATH"

# Install necessary packages and create conda environment
RUN apt-get update -y && \
    apt-get install -y build-essential && \
    conda create --name careamics_gpu python==3.10 pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia && \
    /opt/conda/envs/careamics_gpu/bin/pip install --upgrade pip && \
    /opt/conda/envs/careamics_gpu/bin/pip install careamics

# Activate the conda environment
SHELL ["conda", "run", "-n", "careamics_gpu", "/bin/bash", "-c"]

# Set the entrypoint to use the conda environment
ENTRYPOINT ["/bin/bash", "-c", "source /opt/conda/etc/profile.d/conda.sh && conda activate careamics_gpu && exec \"$@\""]
