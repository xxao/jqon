# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import re
from dataclasses import dataclass
from .register import register
from .query import Query

RE_INDEX = re.compile(r'^(-?\d+)$')


@dataclass
@register("expr")
class Expr(Query):
    """Gets value by sequence of queries."""
    
    queries: list[Query] = ()
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # apply queries
        for query in self.queries:
            data = query(data, *args, **kwargs)
        
        return data
    
    
    @staticmethod
    def parse(expr):
        """Parses expression string."""
        
        # init buff
        queries = []
        
        # remove expression marker
        if expr.startswith("$"):
            expr = expr[1:]
        
        # split parts
        for part in expr.split("."):
            
            # items
            if part.endswith("]"):
                
                # get values
                idx = part.index("[")
                name = part[:idx]
                key = part[idx + 1:-1]
                
                # convert key to int
                if RE_INDEX.match(key):
                    key = int(key)
                
                # add attr query
                if name:
                    queries.append({"attr": name})
                
                # add item query
                queries.append({"item": key})
            
            # calls
            elif part.endswith("()"):
                queries.append({part[:-2]: None})
            
            # attr
            else:
                queries.append({"attr": part})
        
        return queries
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # init from expression
        if isinstance(data, str) and data.startswith("$"):
            data = cls.parse(data)
            return cls(
                queries = [Query.from_json(item) for item in data]
            )
        
        # init from list of queries
        if isinstance(data, list):
            return cls(
                queries = [Query.from_json(item) for item in data]
            )
        
        # init from dict
        if isinstance(data, dict):
            
            # init own dict
            if "expr" in data:
                return cls.from_json(next(iter(data.values())))
            
            # init from single query
            return cls(
                queries = [Query.from_json(data)]
            )
        
        # init as value
        return cls(
            queries = [Query.from_json({"value": data})]
        )
