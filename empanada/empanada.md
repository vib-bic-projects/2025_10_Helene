# Empanada

## Empanada Installation

### Create the environment
```bash
conda create -y -n empanada -c conda-forge python=3.9
conda activate empanada
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia



pip install albumentations>=1.2 pyyaml cztile mlflow opencv-python==4.9.0.80 opencv-python-headless==4.9.0.80 numpy==1.22 scikit-image>=0.19 numba==0.58.1 imagecodecs openpyxl imagehash mlflow simpleitk tqdm
```

### Check if CUDA is installed
```bash
 python -c 'import torch; print(torch.cuda.is_available()); print(torch.backends.cudnn.enabled) '
True
```

```bash
python -c "import torch; x=torch.randn(3,3).to('cuda'); print(x) if torch.cuda.is_available() else print('CUDA not available')"
```

## empanada-napari installation


### Create the environment

```bash
conda create -y -n empanada_napari -c conda-forge python=3.9
conda activate empanada_napari
conda install pyqt
pip install "napari[all]"
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
pip install empanada-napari=1.2
```

### Check if CUDA is installed properly
```bash
 python -c 'import torch; print(torch.cuda.is_available()); print(torch.backends.cudnn.enabled)'
True
```
```bash
python -c "import torch; x=torch.randn(3,3).to('cuda'); print(x) if torch.cuda.is_available() else print('CUDA not available')"
```

## Finetune

### Create patches

```bash
& C:/Users/u0094799/.conda/envs/empanada/python.exe c:/Users/u0094799/Documents/PROJECTS/Leuven/HeleneR/2025_10_Retrain_empanada/code/generate_2d_patches.py 
```

with the configuration:
```python
if __name__ == "__main__":
    extract_2d_patches_from_3d(
        raw_path = "../helene/dataset3-amst2-n2v2-predictions_449.tif",
        label_path = "../helene/groundtruthfinal.tif",#combined_labels_fixed.tif",
        output_folder="empanada_dataset",
        object_name="mito",
        n_patches=512,
        patch_size=(256, 256),
        min_foreground_frac=0.02
    )
```

The patches were splitted, 64 for validation and 448 for training and stored in:

```bash
├───empanada_dataset
│   └───mito
│       ├───images
│       └───masks
├───empanada_validation
│   └───mito
│       ├───images
│       └───masks
```


### Retrain a model

#### With a graphical interface (Napari Plugin empanada-napari)

```bash
conda activate activate empanada_napari
napari
```

Go `Plugins > empanada-napari > Finetune a model`

Set the parameters
```
Model name : helene_mito_02
Train directory : C:\Users\u0094799\Documents\PROJECTS\Leuven\HeleneR\2025_10_Retrain_empanada\code\empanada_dataset
Validation directory : C:\Users\u0094799\Documents\PROJECTS\Leuven\HeleneR\2025_10_Retrain_empanada\code\empanada_validation
Model directory: C:\Users\u0094799\Documents\PROJECTS\Leuven\HeleneR\2025_10_Retrain_empanada\code\model
Model to finetune : MitoNet_v1
FineTune layers : all
Iteration (epoch) : 128
Patch size in pixel : 256
custom config : default config
```

Click on Finetune model

The result will be saved in `C:\Users\u0094799\Documents\PROJECTS\Leuven\HeleneR\2025_10_Retrain_empanada\code\model` as `helene_mito_02.pth` and `helene_mito_02.yaml`

See https://empanada.readthedocs.io/en/latest/tutorials/finetune_tutorial.html#finetuning-the-model


⚠️ : There is no progress bar, check the terminal to see th progression of the finetuning

#### Via Command Line (CLI)
Alternativelly (but to test more)


```bash
& C:/Users/u0094799/.conda/envs/empanada/python.exe c:/Users/u0094799/Documents/PROJECTS/Leuven/HeleneR/2025_10_Retrain_empanada/code/finetune.py c:/Users/u0094799/Documents/PROJECTS/Leuven/HeleneR/2025_10_Retrain_empanada/code/mitonet_finetune_new.yaml
```


## Inference with the retrained mode
Go to `Plugins > empanada-napari > 3d Inference`

use the following parameters

```
model : helene_mito
Fill hole : true
Erode labels : 4
Run orthoplane : true
```

Run twith 2 models, `helene_mito` and the default `MitoNet_v1`

## Metrics

Compare the 2 models

run the script `3D_Segmentation_Quality_from_3D_Stack_from_labels.py`

```bash
& C:/Users/u0094799/.conda/envs/empanada/python.exe c:/Users/u0094799/Documents/PROJECTS/Leuven/HeleneR/2025_10_Retrain_empanada/code/3D_Segmentation_Quality_from_3D_Stack_from_labels.py
```

for both result with `helene_mito` and the default `MitoNet_v1` and with grud truth `labeled_gt.tiff`

All the files are located as an example in :
`C:\Users\u0094799\Documents\PROJECTS\Leuven\HeleneR\2025_10_Retrain_empanada\helene\retrained_result_comparaison`






