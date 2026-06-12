# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from dataclasses import dataclass
from .errors import *
from .register import register
from .query import Query
from .path import Path

UNDEF = object()


@dataclass
@register("var")
class Variable(Query):
    """Keeps value as variable."""
    
    name: str = None
    value: Path | UNDEF = UNDEF
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get variables
        if "variables" not in kwargs:
            kwargs["variables"] = {}
        variables = kwargs["variables"]
        
        # retrieve value from data
        if isinstance(self.value, Query):
            variables[self.name] = self.value(data, *args, **kwargs)
        
        # use value
        elif self.value is not UNDEF:
            variables[self.name] = self.value
        
        # use data
        else:
            variables[self.name] = data
        
        # pass data through
        return data
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get values
        values = next(iter(data.values()))
        
        # use just name
        if isinstance(values, str):
            return cls(
                name = values,
                value = UNDEF
            )
        
        # check values
        if not isinstance(values, list) or len(values) != 2:
            raise QSyntaxError("Variable definition must be a string or [str, any].")
        
        # init instance
        return cls(
            name = values[0],
            value = Path.from_json(values[1])
        )
