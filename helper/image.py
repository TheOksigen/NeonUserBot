# Oğurlama

import os
import asyncio
import pybase64
from PIL import Image
from os.path import basename
from typing import Optional, Tuple


async def convert_toimage(image):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("./downloads/temp.jpg", "jpeg")
    os.remove(image)
    return "./downloads/temp.jpg"
