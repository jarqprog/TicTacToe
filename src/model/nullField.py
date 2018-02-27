from .field import Field


class NullField(Field):
    """Null object."""

    def __init__(self):
        self.symbol = 'null'
