"""Ingestor Interface for the parsers."""
from abc import ABC, abstractmethod
from typing import List

from ..models import QuoteModel


class IngestorInterface(ABC):
    """Abstract class that sets the interface of the parsers."""

    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether a file type in a given path is ingestible."""
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file in a given path."""
        pass
