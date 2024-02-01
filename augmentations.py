import tensorflow as tf
import numpy as np
from scipy import ndimage
import random

@tf.function
def rotate(volume,desired_volume_dims_after_resampling):
    """Rotate the volume by a few degrees"""
    c,h,w = desired_volume_dims_after_resampling
    def scipy_rotate(volume):
        # Define some rotation angles
        angles = [-180,-160,-140,-120,-100,-80,-60,-40,-20, 20, 40, 60, 80 ,100,120,140,160,180]
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

        

    # def random_translate(volume):
    #     # Randomly translate volume
    #     translation = [random.uniform(-1, 1) for _ in range(3)]
    #     volume = ndimage.shift(volume, translation)
    #     return np.resize(volume,(w,h,c))

    def apply_augmentation(volume):
        volume_augmented = volume
        

        # Apply augmentations with a certain probability
        if random.random() < 0.5:
            print("scipy rotate")
            volume_augmented = scipy_rotate(volume_augmented)
        if random.random() < 0.5:
            print("crop")
            volume_augmented = crop_image(volume_augmented)
        # if random.random() < 0.5:
        #     volume_augmented = random_translate(volume_augmented)

        return volume_augmented

    augmented_volume = tf.numpy_function(apply_augmentation, [volume], 'float64')
    return augmented_volume