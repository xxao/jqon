# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from dataclasses import dataclass
from .errors import *
from .register import register
from .query import Query
from .path import Path


@dataclass
@register("=", "==", "!=", ">", "<", ">=", "<=")
@register("eq", "ne", "gt", "lt", "ge", "gte", "le", "lte")
@register("in", "not_in", "contains")
class Binary(Query):
    """Evaluates binary condition to boolean."""
    
    operand: str
    left: Path | None = None
    right: Path | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get left value
        left = data
        if isinstance(self.left, Query):
            left = self.left(data, *args, **kwargs)
        
        # get right value
        right = data
        if isinstance(self.right, Query):
            right = self.right(data, *args, **kwargs)
        
        # equals
        if self.operand in ("=", "==", "eq"):
            return left == right
        
        # not equals
        if self.operand in ("!=", "ne"):
            return left != right
        
        # greater than
        if self.operand in (">", "gt"):
            return left > right
        
        # less than
        if self.operand in ("<", "lt"):
            return left < right
        
        # greater than or equal
        if self.operand in (">=", "ge", "gte"):
            return left >= right
        
        # less than or equal
        if self.operand in ("<=", "le", "lte"):
            return left <= right
        
        # in
        if self.operand == "in":
            return left in right
        
        # not in
        if self.operand == "not_in":
            return left not in right
        
        # contains
        if self.operand == "contains":
            return right in left
        
        # unknown operand
        raise QSyntaxError(f"Unrecognized unary condition operand '{self.operand}'.")
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get values
        operand = next(iter(data))
        values = next(iter(data.values()))
        
        # convert single value
        if not isinstance(values, list):
            values = [values]
        
        # check values
        if not isinstance(values, list) or len(values) not in (1, 2):
            raise QSyntaxError("Binary condition requires one or two values.")
        
        # get values
        if len(values) == 1:
            left = None
            right = values[0]
        else:
            left = values[0]
            right = values[1]
        
        # convert paths
        if left is not None:
            left = Path.from_json(left)
        if right is not None:
            right = Path.from_json(right)
        
        # init instance
        return cls(
            operand = operand,
            left = left,
            right = right
        )
