# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from dataclasses import dataclass
from .errors import *
from .register import register
from .query import Query
from .path import Path


@dataclass
@register("is_true", "true", "is_false", "false")
@register("is_null", "null", "not_null")
@register("is_empty", "empty", "not_empty")
class Unary(Query):
    """Evaluates unary condition to boolean."""
    
    operand: str
    path: Path | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get value
        value = data
        if isinstance(self.path, Query):
            value = self.path(data, *args, **kwargs)
        
        # is true
        if self.operand == "true":
            return bool(value) is True
        
        # is false
        if self.operand == "false":
            return bool(value) is False
        
        # is null
        if self.operand == "null":
            return value is None
        
        # is not null
        if self.operand == "not_null":
            return value is not None
        
        # is empty
        if self.operand == "empty":
            return value in (None, "", [], (), {})
        
        # is not empty
        if self.operand == "not_empty":
            return value not in (None, "", [], (), {})
        
        # unknown operand
        raise QSyntaxError(f"Unrecognized unary condition operand '{self.operand}'.")
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get values
        operand = next(iter(data))
        path = next(iter(data.values()))
        
        # convert to path
        if path is not None:
            path = Path.from_json(path)
        
        # init instance
        return cls(
            operand = operand,
            path = path
        )
