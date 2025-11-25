FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

ENV LC_ALL=C \
    LANG=C \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    TZ=UTC

# Set timezone non-interactively and install dependencies
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get update && apt-get install -y python3-opencv && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install "careamics[examples]"

LABEL Author="Tatiana Woller" \
      Version="1.0" \
      Description="Careamics with PyTorch 2.1.0 and CUDA 11.8 support"

CMD ["/bin/bash"]
