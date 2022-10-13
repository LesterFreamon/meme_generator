"""Genearate Memes."""
from datetime import datetime
import os
import random

from PIL import Image, ImageDraw, ImageFont  # type: ignore[import]


class MemeEngine:
    """Class to create a meme."""

    def __init__(self, output_dir: str):
        """Initialize the meme generator with the output directory."""
        self.output_dir = output_dir

    def make_meme(
            self,
            img_path: str,
            text: str,
            author: str,
            width=500
    ) -> str:
        """Make a meme by pasting a quote on an image."""
        first_name = author.split()[0]
        date_time = datetime.now().strftime('%Y_%m_%d_at_%H_%M_%S')
        file_name = f'{first_name}_{date_time}_{random.randint(0, 1000)}.png'
        image_path = os.path.join(self.output_dir, file_name)
        with Image.open(img_path) as im:
            original_width, original_height = im.size
            if original_width > width:
                new_height = int((width / original_width) * original_height)
                im = im.resize(size=(width, new_height))
            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype('_data/Fonts/FreeMono.ttf', 22)
            draw.text((100, 120), text, font=font)
            draw.text((100, 80), author, font=font)
            im.save(image_path)

        return image_path
