"""Class to keep data parsed from various text files."""


class QuoteModel:
    """Encapsulating the quote data."""

    def __init__(self, author: str, body: str):
        """Object that contains the data parsed from a file."""
        self.author = author
        self.body = body

    def __eq__(self, other) -> bool:
        """Compare two objects."""
        return (self.author == other.author) and (self.body == other.body)

    def __str__(self) -> str:
        """Crate string representation."""
        return f'QuoteModel(author={self.author}, body={self.body})'

    def __repr__(self) -> str:
        """Crate string representation."""
        return str(self)
