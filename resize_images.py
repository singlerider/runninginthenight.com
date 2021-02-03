#!/usr/bin/env python

"""
This command requires an installation of ImageMagick.

It will resize an image whose path is accepted as the first argument. It will output a file at the same path, with ".converted" appended to the end. There is an optional second argument for the image width in pixels, where the default is 1000. Proportions will be maintained.
"""

import os
import subprocess
import sys

from PIL import Image


def convert_image(image_path, image_max_dimension=500):
    image = Image.open(image_path)
    width, height = image.size
    aspect_ratio = 1.0
    new_width = None
    new_height = None
    print(image_path, width, height)
    if width > height:
        aspect_ratio = width / height
        new_width = image_max_dimension
        new_height = new_width / aspect_ratio
    else:
        aspect_ratio = height / width
        new_height = image_max_dimension
        new_width = new_height / aspect_ratio
    image = image.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
    output_filename = image_path
    image.save(output_filename)


if __name__ == "__main__":
    image_directory_path = sys.argv[1]
    image_max_dimension = 500
    if len(sys.argv) > 2:
        image_max_dimension = int(sys.argv[2])
    for image_filepath in os.listdir(image_directory_path):
        if ".DS_Store" in image_filepath:
            continue
        full_image_path = os.path.join(image_directory_path, image_filepath)
        convert_image(full_image_path, image_max_dimension=image_max_dimension)
