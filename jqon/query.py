# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import json
from .errors import *
from .register import QUERIES


class Query(object):
    """Baseclass for all queries."""
    
    
    def __call__(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # init global variables
        if not "variables" in kwargs:
            kwargs["variables"] = {}
        
        # apply query
        return self.apply(data, *args, **kwargs)
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        return data
    
    
    @classmethod
    def from_text(cls, data):
        """Initialize instance from JSON text."""
        
        # init from JSON
        return cls.from_json(json.loads(data))
    
    
    @staticmethod
    def from_json(data):
        """Initialize instance from JSON."""
        
        # sequence of queries
        if isinstance(data, list):
            q_type = "path"
        
        # path expression
        elif isinstance(data, str) and data.startswith("$"):
            q_type = "path"
        
        # not query
        elif not isinstance(data, dict) or len(data) != 1:
            raise QSyntaxError(f"Unrecognized query syntax '{data}'.")
        
        # single query
        else:
            q_type = next(iter(data))
        
        # get class
        q_cls = QUERIES.get(q_type, None)
        if q_cls is None:
            raise QSyntaxError(f"Unrecognized query type '{q_type}'.")
        
        # init instance
        inst = q_cls.from_json(data)
        
        return inst
