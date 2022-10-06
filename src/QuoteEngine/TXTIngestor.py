"""Ingest txt files."""
from typing import List

from .helpers import can_ingest, parse_decorater, parse_unstructured_text_pager
from .IngestorInterface import IngestorInterface
from ..models import QuoteModel


class TXTIngestor(IngestorInterface):
    """TXT file ingestor."""

    suffixes = {'.txt'}

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether the given path holds a txt format."""
        return can_ingest(path, cls.suffixes)

    @classmethod
    @parse_decorater('txt')
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a txt file of a given file path.

        Args:
            path: The file path.

        Returns:
            A list of objects, each pertaining to a diff row of the file
        """
        with open(path, 'r') as txt_file:
            quote_models = parse_unstructured_text_pager(txt_file)

        return quote_models
