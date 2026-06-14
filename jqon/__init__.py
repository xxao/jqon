# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

version = (0, 2, 0)

from .errors import *
from .register import register
from .query import Query
from .value import Value
from .variable import Variable
from .expression import Expr
from .getters import Attr, Item
from .unary import Unary
from .binary import Binary
from .logical import AND, OR, NOT
from .funcs import Bool, Len, Any, All, Min, Max, Sum, Avg
from .enumerable import Take, Skip, Slice
from .enumerable import Select, Many, Where, Distinct
from .enumerable import Single, First, Last, Count


# init shortcuts
def from_text(text):
    """Initialize query from text."""
    
    return Query.from_text(text)


def from_json(data):
    """Initialize query from JSON."""
    
    return Query.from_json(data)
