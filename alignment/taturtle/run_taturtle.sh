#!/bin/bash

python main.py --x_a 40 126 --y_a  2543 2672 --search_window 100 --alpha 1.0 --to_crop False --thick_corr True --slice_thickness 6.0 --cpu 8 --img_ref "/path_to_your_raw_dataset/slice_00200_z=1.0995um.tif"
