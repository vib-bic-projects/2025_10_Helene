import numpy as np
import tifffile
import pandas as pd
from pathlib import Path

def extract_2d_patches_from_3d(
    raw_path,
    label_path,
    output_folder="empanada_dataset",
    object_name="object",
    n_patches=64,
    patch_size=(256, 256),
    min_foreground_frac=0.01,
    rng=None
):
    """
    Extract random 2D patches (XY) from a 3D raw + label stack for Empanada finetuning.

    Parameters
    ----------
    raw_path : str or Path
        Path to 3D raw image TIFF.
    label_path : str or Path
        Path to 3D label TIFF (same shape).
    output_folder : str or Path
        Folder where images/ and labels/ subfolders will be created.
    n_patches : int
        Total number of 2D patches to extract.
    patch_size : tuple of int
        (height, width) of each patch.
    min_foreground_frac : float
        Minimum fraction of nonzero label pixels to keep a patch.
    rng : np.random.Generator or None
        Optional random generator for reproducibility.
    """
    if rng is None:
        rng = np.random.default_rng()

    output_folder = Path(output_folder)
    img_dir = output_folder / object_name / "images"
    lbl_dir = output_folder / object_name / "masks"
    img_dir.mkdir(parents=True, exist_ok=True)
    lbl_dir.mkdir(parents=True, exist_ok=True)

    # Load the data
    raw = tifffile.imread(raw_path)
    label = tifffile.imread(label_path)

    if raw.shape != label.shape:
        raise ValueError(f"Raw and label must have same shape, got {raw.shape} vs {label.shape}")

    Z, Y, X = raw.shape
    ph, pw = patch_size

    coords = []
    patch_count = 0
    attempts = 0
    max_attempts = n_patches * 50

    while patch_count < n_patches and attempts < max_attempts:
        attempts += 1

        z = rng.integers(0, Z)
        y0 = rng.integers(0, Y - ph + 1)
        x0 = rng.integers(0, X - pw + 1)

        raw_patch = raw[z, y0:y0+ph, x0:x0+pw]#.astype(np.uint16)
        label_patch = label[z, y0:y0+ph, x0:x0+pw].astype(np.uint8)

        # Skip empty patches
        fg_frac = np.mean(label_patch > 0)
        if fg_frac < min_foreground_frac:
            continue

        # Normalize intensity (0–1)
        #if raw_patch.max() > raw_patch.min():
        #    raw_patch = (raw_patch - raw_patch.min()) / (raw_patch.max() - raw_patch.min())
        #else:
        #    continue  # flat patch

        # Save files
        patch_id = f"{patch_count:03d}"
        tifffile.imwrite(img_dir / f"patch_{patch_id}.tif", raw_patch)
        tifffile.imwrite(lbl_dir / f"patch_{patch_id}.tif", label_patch)

        coords.append({
            "patch_id": patch_id,
            "z_index": int(z),
            "y0": int(y0),
            "x0": int(x0),
            "foreground_frac": float(fg_frac)
        })
        patch_count += 1

    # Save CSV with patch info
    csv_path = output_folder / "patch_metadata.csv"
    pd.DataFrame(coords).to_csv(csv_path, index=False)

    print(f"✅ Saved {patch_count} 2D patches to '{output_folder}'")
    print(f"📁 Images: {img_dir}")
    print(f"📁 Labels: {lbl_dir}")
    print(f"📄 Metadata: {csv_path}")

    return coords


# Example usage:
#conda activate empanada
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
