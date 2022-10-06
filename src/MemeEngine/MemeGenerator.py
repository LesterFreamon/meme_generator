"""Genearate Memes."""
from PIL import Image

class MemeGenerator:

    def __init__(self, output_dir: str):
        self.output_dir = output_dir

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
