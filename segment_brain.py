from skimage import morphology
import pydicom
import numpy as np
from scipy import ndimage

def segment(brain_image):
    segmentation = morphology.dilation(brain_image, np.ones((1,1)))
    labels, label_nb = ndimage.label(segmentation)
    label_count = np.bincount(labels.ravel().astype('int'))
    # The size of label_count is the number of classes/segmentations found
    
    # We don't use the first class since it's the background
    label_count[0] = 0
    
    # We create a mask with the class with more pixels
    # In this case should be the brain
    mask = labels == label_count.argmax()

    # Improve the brain mask
    mask = morphology.dilation(mask, np.ones((5, 5)))
    mask = ndimage.morphology.binary_fill_holes(mask)
    mask = morphology.dilation(mask, np.ones((3, 3)))
    # masked_image = mask * brain_image

    return mask
