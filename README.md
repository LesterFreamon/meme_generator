# Meme Generator

## Overview

An application that dynamically generates memes from a stock of images and quotes. 

## Table of Contents

- [Setup](#Setup)
- [Usage](#usage)
- [Testing](#Testing)
- [License](#license)

## Setup

### Download the repository
```shell
git clone https://github.com/LesterFreamon/meme_generator.git
```

### Required Installations
Install pdf reader:

Windows: download from [https://www.xpdfreader.com/download.html](https://www.xpdfreader.com/download.html)

Linux: 
```shell
sudo apt-get install -y xpdf
```

Mac OS:
```shell
brew install xpdf
```

### Setup Virtual Environment:
* Go to the project root directory
* Create the virtual environment```python3 -m venv ./venv```
* Run env: ```source .venv/bin/activate```
* Install packages: ```pip install -r requirements.txt```

## Usage
From within the virtual environment.
### Web App
```shell
python app.py
```

### Command Line
```shell
python meme.py --body <body> --author <author> --path <path>
```

## Testing
All of the tests and linters can be executed by running the following script:
```shell
bash ./validator.sh
```
---


## Badges

![badmath](https://img.shields.io/github/languages/top/lernantino/badmath)

Badges aren't necessary, per se, but they demonstrate street cred. Badges let other developers know that you know what
you're doing. Check out the badges hosted by [shields.io](https://shields.io/). You may not understand what they all
represent now, but you will in time.

## Features

If your project has a lot of features, list them here.

## How to Contribute

If you created an application or package and would like other developers to contribute it, you can include guidelines
for how to do so. The [Contributor Covenant](https://www.contributor-covenant.org/) is an industry standard, but you can
always write your own if you'd prefer.
