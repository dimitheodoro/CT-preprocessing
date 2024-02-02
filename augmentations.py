import tensorflow as tf
import numpy as np
from scipy import ndimage
import random
from scipy.ndimage import gaussian_filter

@tf.function
def CT_augmentations(volume):
    """Rotate the volume by a few degrees"""
    
    def scipy_rotate(volume):
        # Define some rotation angles
        angles = [-20, -10, -5, 5, 10, 20]
        # Pick an angle at random
        angle = random.choice(angles)
        # Rotate volume
        volume = ndimage.rotate(volume, angle, reshape=False)
        volume[volume < 0] = 0
        volume[volume > 1] = 1
        return volume


    def crop_image(image):
        # Get original image dimensions
        original_height, original_width = image.shape[:2]
        # Generate random coordinates for cropping
        crop_top = random.randint(0, original_height // 2)
        crop_left = random.randint(0, original_width // 2)
        crop_height = random.randint(1, original_height - crop_top)
        crop_width = random.randint(1, original_width - crop_left)
        # Calculate bottom and right coordinates of the cropping region
        crop_bottom = min(original_height, crop_top + crop_height)
        crop_right = min(original_width, crop_left + crop_width)
        # Crop the image
        cropped_image = image[crop_top:crop_bottom, crop_left:crop_right]
        # Pad cropped region if necessary to match original shape
        cropped_image_padded = np.zeros((original_height, original_width, image.shape[2]), dtype=image.dtype)
        cropped_image_padded[crop_top:crop_bottom, crop_left:crop_right] = cropped_image
        return cropped_image_padded
    
    def gaussianfilter(volume):
        return gaussian_filter(volume, sigma=1)

    def clipped_zoom(img, zoom_factor, **kwargs):
        h, w = img.shape[:2]
        # For multichannel images we don't want to apply the zoom factor to the RGB
        # dimension, so instead we create a tuple of zoom factors, one per array
        # dimension, with 1's for any trailing dimensions after the width and height.
        zoom_tuple = (zoom_factor,) * 2 + (1,) * (img.ndim - 2)
        # Zooming out
        if zoom_factor < 1:
            # Bounding box of the zoomed-out image within the output array
            zh = int(np.round(h * zoom_factor))
            zw = int(np.round(w * zoom_factor))
            top = (h - zh) // 2
            left = (w - zw) // 2
            # Zero-padding
            out = np.zeros_like(img)
            out[top:top+zh, left:left+zw] = ndimage.zoom(img, zoom_tuple, **kwargs)
        # Zooming in
        elif zoom_factor > 1:
            # Bounding box of the zoomed-in region within the input array
            zh = int(np.round(h / zoom_factor))
            zw = int(np.round(w / zoom_factor))
            top = (h - zh) // 2
            left = (w - zw) // 2
            out = ndimage.zoom(img[top:top+zh, left:left+zw], zoom_tuple, **kwargs)
            # `out` might still be slightly larger than `img` due to rounding, so
            # trim off any extra pixels at the edges
            trim_top = ((out.shape[0] - h) // 2)
            trim_left = ((out.shape[1] - w) // 2)
            out = out[trim_top:trim_top+h, trim_left:trim_left+w]
        # If zoom_factor == 1, just return the input array
        else:
            out = img
        return out


    def apply_augmentation(volume):
        volume_augmented = volume

        # Apply augmentations with a certain probability
        if random.random() < 0.5:
            print("scipy_rotate")
            volume_augmented = scipy_rotate(volume_augmented)
        if random.random() < 0.5:
            print("crop_image")
            volume_augmented = crop_image(volume_augmented)
        if random.random() < 0.5:
            print("clipped_zoom")
            volume_augmented = clipped_zoom(volume_augmented,1.5)
        if random.random() < 0.5:
            print("blur")
            volume_augmented = gaussianfilter(volume_augmented)

        return volume_augmented

    augmented_volume = tf.numpy_function(apply_augmentation, [volume], 'float64')
    return augmented_volume