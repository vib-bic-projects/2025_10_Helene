from squirrel.workflows.elastix import stack_alignment_validation_workflow
from squirrel.library.rois import list2roi
import os

stack='/input_path' # to change to your data
out_dirpath='/output_path' #output

# Now with the fixed TiffStack, we can use the proper ROI format
rois= [list2roi([0,24,1418,500,256,256])] # rawtop, amst2top
#rois= [list2roi([0,30,1418,500,256,256])] # taturtle top

print(os.listdir(stack))
stack_alignment_validation_workflow(
        stack,
        out_dirpath,
        rois,
        key='data',
        pattern='slice_*.tif',
        resolution_yx=(1.0, 1.0),
        out_name='testval',
        y_max=10,
        method='elastix',
        gaussian_sigma=1.0,
        subtract_average=False,
        verbose=False
)
