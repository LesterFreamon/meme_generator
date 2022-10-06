"""Yet to be implemented."""
from typing import List, Optional

from .IngestorInterface import IngestorInterface
from ..models import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """A class that allows one generic form to parse files."""

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> Optional[List[QuoteModel]]:
        """Parse with the correct ingestor."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
