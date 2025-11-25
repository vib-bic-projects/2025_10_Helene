# based on this notebook: https://careamics.github.io/0.1/applications/Noise2Void/SEM/

from pathlib import Path
import numpy as np
import tifffile
from careamics import CAREamist
from careamics.config import create_n2v_configuration
from careamics_portfolio import PortfolioManager
from PIL import Image

# and download the data
root_path = Path("pathway_where_you_want to save the model") # to modify

# create paths for the data
data_path = Path(root_path / "folder_of_input_dataset") # to modify
train_path = data_path / "training"
val_path = data_path / "val"

image_train=tifffile.imread("/pathway_input_dataset/training/training.tif") # to modify
train_image_array=image_train[0]

portfolio = PortfolioManager()
portfolio.denoising.N2V_SEM.description

general_description = (
    "This model is a UNet trained using the Noise2Void algorithm to denoise "
    "images. The training data consists of crops from an SEM dataset "
    "Nalan Liv. The notebook used to "
    "train this model is available on the CAREamics documentation website; "
    "find it at the following link: "
    "https://careamics.github.io/0.1/applications/Noise2Void/SEM/."
)

config = create_n2v_configuration(
    experiment_name="nalan_stack3",
    data_type="tiff",
    axes="SYX",
    patch_size=(64, 64),
    batch_size=64,
    num_epochs=100,
    use_n2v2=True,
)

print(config)

# instantiate a CAREamist
careamist = CAREamist(source=config)

# train
careamist.train(
    train_source=train_path,
    val_source=val_path,
)

# Export the model",
careamist.export_to_bmz(
    path_to_archive="sem_n2v2_model.zip",
    friendly_model_name="SEM_N2V2",
    input_array=image_train.astype(np.float32),
    authors=[{"name": "TW and BP", "affiliation": "VIB BIC"}],
    general_description=general_description,
    data_description=portfolio.denoising.N2V_SEM.description
)
