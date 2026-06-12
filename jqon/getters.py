# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from dataclasses import dataclass
from .register import register
from .query import Query


@dataclass
@register("attr")
class Attr(Query):
    """Gets attribute by name."""
    
    name: str = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get variables
        variables = kwargs.get("variables", {})
        
        # get from variables
        if self.name in variables:
            return variables[self.name]
        
        # get from data
        else:
            data = getattr(data, self.name)
        
        return data
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # init instance
        return cls(
            name = next(iter(data.values()))
        )


@dataclass
@register("item")
class Item(Query):
    """Gets item by key."""
    
    key: str | int = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        return data[self.key]
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # init instance
        return cls(
            key = next(iter(data.values()))
        )
