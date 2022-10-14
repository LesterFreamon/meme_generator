"""Create memes random memes on random images."""
import os
import random
from typing import List, Optional

from src.MemeEngine.MemeEngine import MemeEngine  # type: ignore
from src.QuoteEngine.Ingestor import Ingestor  # type: ignore
from src.models import QuoteModel  # type: ignore

from argparse import ArgumentParser


def generate_meme(
        path: Optional[str] = None,
        body: Optional[str] = None,
        author: Optional[str] = None
) -> str:
    """Generate a meme given a path and a quote."""
    img = None
    quote = None
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes: List[QuoteModel] = []
        for quote_file in quote_files:
            tmp_quotes = Ingestor.parse(quote_file)
            if tmp_quotes is not None:
                quotes.extend(tmp_quotes)

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
