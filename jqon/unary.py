# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from dataclasses import dataclass
from .errors import *
from .register import register
from .query import Query
from .expression import Expr


@dataclass
@register("is_true", "true", "is_false", "false")
@register("is_null", "null", "not_null")
@register("is_empty", "empty", "not_empty")
class Unary(Query):
    """Evaluates unary condition to boolean."""
    
    operand: str
    expr: Expr | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get value
        value = data
        if isinstance(self.expr, Query):
            value = self.expr(data, *args, **kwargs)
        
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
        expr = next(iter(data.values()))
        
        # convert to expr
        if expr is not None:
            expr = Expr.from_json(expr)
        
        # init instance
        return cls(
            operand = operand,
            expr = expr
        )
