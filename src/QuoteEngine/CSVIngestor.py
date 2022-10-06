"""Ingest CSV Files."""
import csv
from typing import List

from .helpers import can_ingest, parse_decorater, check_fieldnames
from .IngestorInterface import IngestorInterface
from .singleton import AUTHOR_FIELD, BODY_FIELD
from ..models import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSV file ingestor."""

    suffixes = {'.csv'}

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether the given path holds a csv format."""
        return can_ingest(path, cls.suffixes)

    @classmethod
    @parse_decorater('csv')
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a csv file of a given file path.

        Args:
            path: The file path.

        Returns:
            List of objects, each pertaining to a diff row of the file
        """
        quote_models = []
        with open(path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            check_fieldnames(reader.fieldnames)
            for row in reader:
                quote_models.append(
                    QuoteModel(row[AUTHOR_FIELD], row[BODY_FIELD])
                )

        return quote_models
