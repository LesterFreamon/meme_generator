"""Ingest docx files."""
from typing import List

import docx

from .helpers import can_ingest, parse_decorater, parse_unstructured_text_pager
from .IngestorInterface import IngestorInterface
from ..models import QuoteModel


class DocxIngestor(IngestorInterface):
    """DOCX file ingestor."""

    suffixes = {'.docx'}

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether the given path holds a docx format."""
        return can_ingest(path, cls.suffixes)

    @classmethod
    @parse_decorater('docx')
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a txt file of a given file path.

        Args:
            path: The file path.

        Returns:
            A list of objects, each pertaining to a diff row of the file
        """
        document = docx.Document(path)
        quote_models = parse_unstructured_text_pager(
            map(lambda x: x.text.replace('"', ''), document.paragraphs)
        )
        return quote_models
