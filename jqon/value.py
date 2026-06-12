# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from dataclasses import dataclass
from typing import Any
from .register import register
from .query import Query


@dataclass
@register("value")
class Value(Query):
    """Returns defined value."""
    
    value: Any = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # use value
        return self.value
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # init instance
        return cls(
            value = next(iter(data.values()))
        )
