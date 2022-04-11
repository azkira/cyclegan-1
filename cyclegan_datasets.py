"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
    'sketch2photo_train': 188,
    'sketch2photo_test': 188
}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
    'sketch2photo_train': '.png',
    'sketch2photo_test': '.jpg',
}

"""The path to the output csv file."""
PATH_TO_CSV = {
    'sketch2photo_train': './CycleGAN_TensorFlow/input/sketch2photo/sketch2photo_train.csv',
    'sketch2photo_test': './CycleGAN_TensorFlow/input/sketch2photo/sketch2photo_test.csv',
}
