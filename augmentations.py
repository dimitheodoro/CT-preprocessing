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
        angles = [-20, -10, -5, 5, 10, 20]
        # Pick an angle at random
        angle = random.choice(angles)
        # Rotate volume
        volume = ndimage.rotate(volume, angle, reshape=False)
        volume[volume < 0] = 0
        volume[volume > 1] = 1
        return volume

    def random_flip(volume):
        # Randomly flip volume along axis
        axis = random.choice([0, 1, 2])
        volume = np.flip(volume, axis)
        return np.resize(volume,(w,h,c))

    def random_scale(volume):
        # Scale volume by a random factor between 0.8 and 1.2
        factor = random.uniform(0.8, 1.2)
        volume = ndimage.zoom(volume, factor)
        return np.resize(volume,(w,h,c))

    def random_translate(volume):
        # Randomly translate volume
        translation = [random.uniform(-10, 10) for _ in range(3)]
        volume = ndimage.shift(volume, translation)
        return np.resize(volume,(w,h,c))

    def apply_augmentation(volume):
        volume_augmented = volume

        # Apply augmentations with a certain probability
        if random.random() < 0.5:
            volume_augmented = scipy_rotate(volume_augmented)
        if random.random() < 0.5:
            volume_augmented = random_flip(volume_augmented)
        if random.random() < 0.5:
            volume_augmented = random_scale(volume_augmented)
        if random.random() < 0.5:
            volume_augmented = random_translate(volume_augmented)

        return volume_augmented

    augmented_volume = tf.numpy_function(apply_augmentation, [volume], 'float64')
    return augmented_volume