"""Run an app that generates random memes on random images."""
from datetime import datetime
import os
import random
import requests
from flask import Flask, render_template, abort, request

from src.QuoteEngine.Ingestor import Ingestor
from src.MemeEngine.MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for quote_file in quote_files:
        quotes.extend(Ingestor.parse(quote_file))

    images_path = "_data/photos/dog/"

    imgs = []
    for file in os.listdir(images_path):
        if file.endswith('jpeg'):
            imgs.append(os.path.join(images_path, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    if not request.form['image_url']:
        return render_template('meme_form.html')

    img_url = request.form['image_url']
    try:
        r = requests.get(img_url, verify=False)
    except requests.exceptions.InvalidURL:
        print("InvalidURL: Could not retrieve and image from the given url.")
        return render_template('meme_error.html')
    file_name = datetime.now().strftime('%Y_%m_%d_at_%H_%M_%S')
    file_path = f'./tmp/{file_name}.jpg'
    with open(file_path, 'w') as f:
        f.write(r.content)

    author = request.form['author']
    body = request.form['body']
    path = meme.make_meme(file_path, body, author)
    os.remove(file_path)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
