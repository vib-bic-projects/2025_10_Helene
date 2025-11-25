# based on the following notebook https://careamics.github.io/0.1/applications/Noise2Void/SEM/

import numpy as np
import tifffile
from careamics import CAREamist
from careamics.config import create_n2v_configuration
from careamics import model_io
from PIL import Image
from pathlib import Path

# and download the data
root_path = Path("pathway_data") # to modify

# create paths for the data
data_path = Path(root_path / "folder_to_your_data)")  # to modify
test_path = "/pathway_to_your_data_to_denoise" # to modify and should be different from training data

careamics_bmz= CAREamist("/pathway_where_you_saved_your_model/sem_n2v2_model.zip") # to modify
prediction = careamics_bmz.predict_to_disk(source=test_path, tile_size=(256, 256), tile_overlap=(48, 48))
