# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from dataclasses import dataclass
from .errors import *
from .register import register
from .query import Query


@dataclass
class Logical(Query):
    """Defines base class for logical queries."""
    
    queries: list[Query] = ()
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get queries
        queries = next(iter(data.values()))
        
        # check queries
        if not isinstance(queries, list):
            raise QSyntaxError("Logical operation definition must be a list of queries.")
        
        # init instance
        return cls(
            queries = [Query.from_json(item) for item in queries]
        )


@dataclass
@register("AND", "and")
class AND(Logical):
    """Evaluates sequence of conditions with AND."""
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        for query in self.queries:
            if not query(data, *args, **kwargs):
                return False
        
        return True


@dataclass
@register("OR", "or")
class OR(Logical):
    """Evaluates sequence of conditions with OR."""
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        for query in self.queries:
            if query(data, *args, **kwargs):
                return True
        
        return False


@dataclass
@register("NOT", "not")
class NOT(Logical):
    """Evaluates sequence of conditions with NOT."""
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        for query in self.queries:
            if query(data, *args, **kwargs):
                return False
        
        return True
