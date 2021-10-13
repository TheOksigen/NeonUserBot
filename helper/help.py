# CopyRight (C) GNU License.
# NeonUserBot
# Nusrte
# 

import os
import random
import asyncio
import pybase64
import PIL.ImageOps
from PIL import Image
from os.path import basename
from random import choice, randint
from typing import Optional, Tuple


async def convert_toimage(image):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("./downloads/temp.jpg", "jpeg")
    os.remove(image)
    return "./downloads/temp.jpg"

# --------------------------------#

async def random_color():
    number_of_colors = 2
    return [
        "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
        for i in range(number_of_colors)
    ]

# ------------------------------ #

async def grayscale(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.grayscale(image)
    inverted_image.save(endname)

# ------------------------------ #


