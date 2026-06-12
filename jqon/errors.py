# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.


class QError(Exception):
    """Represents a jqson exception base."""
    pass


class QSyntaxError(QError):
    """Represents an incorrect syntax exception."""
    pass


class QUndefError(QError):
    """Represents a missing definition exception."""
    pass


class QIterError(QError):
    """Represents an iteration exception."""
    pass
