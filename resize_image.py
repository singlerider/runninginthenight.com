#!/usr/bin/env python

"""
This command requires an installation of ImageMagick.

It will resize an image whose path is accepted as the first argument. It will output a file at the same path, with ".converted" appended to the end. There is an optional second argument for the image width in pixels, where the default is 1000. Proportions will be maintained.
"""


import subprocess
import sys


def convert_image(image_path, image_width=1000):
    output_filename = f"{image_path}.converted"
    subprocess.run(
        [
            "convert", "-resize", str(image_width),
            image_path, output_filename
        ], stdout=subprocess.PIPE, text=True
    )


if __name__ == "__main__":
    image_path = sys.argv[1]
    image_width = 1000
    if len(sys.argv) > 2:
        image_width = int(sys.argv[2])
    convert_image(image_path, image_width=image_width)