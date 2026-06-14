# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from dataclasses import dataclass
from .register import register
from .query import Query
from .expression import Expr


@dataclass
@register("bool")
class Bool(Query):
    """Returns boolean value of data."""
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        return bool(data)
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        return cls()


@dataclass
@register("len")
class Len(Query):
    """Returns length of given sequence."""
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        return len(data)
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        return cls()


@dataclass
@register("min")
class Min(Query):
    """Returns minimum item from given sequence."""
    
    key: Expr | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get values
        key = None
        if isinstance(self.key, Query):
            key = lambda d: self.key(d, *args, **kwargs)
        
        # apply
        return min(data, key=key)
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        value = next(iter(data.values()))
        
        # init instance
        return cls(
            key = Expr.from_json(value) if value is not None else None
        )


@dataclass
@register("max")
class Max(Query):
    """Returns maximum item from given sequence."""
    
    key: Expr | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get values
        key = None
        if isinstance(self.key, Query):
            key = lambda d: self.key(d, *args, **kwargs)
        
        # apply
        return max(data, key=key)
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        value = next(iter(data.values()))
        
        # init instance
        return cls(
            key = Expr.from_json(value) if value is not None else None
        )
