"""Create memes random memes on random images."""
import os
import random

from src.MemeEngine.MemeEngine import MemeEngine
from src.QuoteEngine.Ingestor import Ingestor
from src.models import QuoteModel

from argparse import ArgumentParser


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/txt_file.txt',
                       './_data/DogQuotes/docx_file.docx',
                       './_data/DogQuotes/pdf_file.pdf',
                       './_data/DogQuotes/csv_file.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = ArgumentParser(description="Generate a meme.")
    parser.add_argument(
        '--body', type=str, default=None, help="The quote on the meme."
    )
    parser.add_argument(
        '--author', type=str, default=None, help="The author of the quote."
    )
    parser.add_argument(
        '--path',
        type=str,
        default=None,
        help="Path for the image you wish the quote to be displayed in."
    )
    args = parser.parse_args()
    print(args.path)
    print(generate_meme(args.path, args.body, args.author))
