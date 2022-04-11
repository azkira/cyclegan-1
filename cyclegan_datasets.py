"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
    'horse2zebra_train': 88,
    'horse2zebra_test': 100
}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
    'horse2zebra_train': '.png',
    'horse2zebra_test': '.jpg',
}

"""The path to the output csv file."""
PATH_TO_CSV = {
    'horse2zebra_train': './CycleGAN_TensorFlow/input/sketch2photo/sketch2photo_train.csv',
    'horse2zebra_test': './CycleGAN_TensorFlow/input/sketch2photo/sketch2photo_test.csv',
}
