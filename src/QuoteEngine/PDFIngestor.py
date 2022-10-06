"""Ingest PDF files."""
import os
import random
import subprocess
from typing import List

from .helpers import can_ingest, parse_decorater, parse_unstructured_text_pager
from .IngestorInterface import IngestorInterface
from ..models import QuoteModel


class PDFIngestor(IngestorInterface):
    """PDF file ingestor."""

    suffixes = {'.pdf'}

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether the given path holds a pdf format."""
        return can_ingest(path, cls.suffixes)

    @classmethod
    @parse_decorater('pdf')
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a pdf file of a given file path.

        Args:
            path: The file path.

        Returns:
            A list of objects, each pertaining to a diff row of the file
        """
        tmp_file_path = f'./tmp{random.randint(0, 100000000)}.txt'
        subprocess.call(['pdftotext', path, tmp_file_path])
        with open(tmp_file_path, 'r') as pdf_file:
            line_generator = map(
                lambda x: x.strip('\n\r').strip(), pdf_file.readlines()
            )
            quote_models = parse_unstructured_text_pager(line_generator)
        os.remove(tmp_file_path)
        return quote_models
