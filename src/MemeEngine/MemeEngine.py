"""Genearate Memes."""
from datetime import datetime
import os
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont  # type: ignore[import]

from ..QuoteEngine.singleton import TEXT_START_FONT


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
            font = ImageFont.truetype(
                '_data/Fonts/FreeMono.ttf', TEXT_START_FONT
            )
            max_char_count = int(im.size[0] / TEXT_START_FONT)
            text = textwrap.fill(text=text, width=max_char_count)
            num_lines = text.count('\n') + 1

            txt_x = im.width // 3
            txt_y = im.height // 3
            author_y = txt_y + (TEXT_START_FONT * num_lines)
            draw.text((txt_x, txt_y), text, font=font)
            draw.text((txt_x, author_y), author, fill='gray', font=font)
            im.save(image_path)

        return image_path
