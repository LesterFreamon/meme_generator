"""Helper functions for the ingestors."""
import os
import pathlib
from typing import Any, Callable, Iterator, List, Optional, Sequence, Set

from .IngestorInterface import IngestorInterface
from .singleton import AUTHOR_FIELD, BODY_FIELD
from ..models import QuoteModel


def can_ingest(path: str, ingest_suffixes: Set[str]) -> bool:
    """Check if the given path holds a file type with a given suffix."""
    correct_suffix = pathlib.Path(path).suffix in ingest_suffixes
    if os.path.exists(path) and os.path.isfile(path) and correct_suffix:
        return True

    return False


def check_fieldnames(file_fieldsnames: Optional[Sequence[str]]) -> None:
    """Check if all of the required fields are found."""
    if file_fieldsnames is None:
        raise ValueError(f'File is empty')

    if AUTHOR_FIELD not in file_fieldsnames:
        raise ValueError(f'"{AUTHOR_FIELD}" field could not be found in file')

    if BODY_FIELD not in file_fieldsnames:
        raise ValueError(f'"{BODY_FIELD}" field could not be found in file')


def parse_text_line(line: str) -> QuoteModel:
    """Parse one line of text."""
    if '-' not in line:
        raise ValueError(f'{line} cannot be parsed.')

    body, author = line.split('-')
    author = author.strip()
    body = body.strip()
    return QuoteModel(author, body)


def parse_unstructured_text_pager(lines: Iterator[str]) -> List[QuoteModel]:
    """Parse an iterator that contains one line in every iteration."""
    quote_models = []
    for line in lines:
        try:
            quote_model = parse_text_line(line)
            quote_models.append(quote_model)
        except ValueError as e:
            print(str(e))

    return quote_models


def parse_decorater(file_type: str) -> Any:
    """Decorate a file checker."""

    def parse_checker(
            method: Callable[[IngestorInterface, str], List[QuoteModel]]
    ) -> Callable[[IngestorInterface, str], List[QuoteModel]]:
        """Check that file in filepath can be parsed."""

        def inner(cls: IngestorInterface, path: str) -> List[QuoteModel]:
            """Check whether the path can be parsed."""
            if not cls.can_ingest(path):
                if len(path) < 12:
                    path_rep = path
                else:
                    path_rep = '...' + path[-11:]
                raise ValueError(
                    f'{path_rep} does not contain a {file_type} file'
                )

            return method(cls, path)

        return inner

    return parse_checker
