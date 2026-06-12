# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from dataclasses import dataclass
from .register import register
from .query import Query
from .path import Path


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
@register("any")
class Any(Query):
    """Returns True if any item of given sequence evaluates to True."""
    
    path: Path | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get values
        if isinstance(self.path, Query):
            data = (self.path(item, *args, **kwargs) for item in data)
        
        # apply
        return any(data)
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        value = next(iter(data.values()))
        
        # init instance
        return cls(
            path = Path.from_json(value) if value is not None else None
        )


@dataclass
@register("all")
class All(Query):
    """Returns True if all items of given sequence evaluate to True."""
    
    path: Path | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get values
        if isinstance(self.path, Query):
            data = (self.path(item, *args, **kwargs) for item in data)
        
        # apply
        return all(data)
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        value = next(iter(data.values()))
        
        # init instance
        return cls(
            path = Path.from_json(value) if value is not None else None
        )


@dataclass
@register("min")
class Min(Query):
    """Returns minimum item from given sequence."""
    
    key: Path | None = None
    
    
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
            key = Path.from_json(value) if value is not None else None
        )


@dataclass
@register("max")
class Max(Query):
    """Returns maximum item from given sequence."""
    
    key: Path | None = None
    
    
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
            key = Path.from_json(value) if value is not None else None
        )


@dataclass
@register("sum")
class Sum(Query):
    """Returns sum of all items of given sequence."""
    
    path: Path | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get values
        if isinstance(self.path, Query):
            data = (self.path(item, *args, **kwargs) for item in data)
        
        # apply
        return sum(data)
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        value = next(iter(data.values()))
        
        # init instance
        return cls(
            path = Path.from_json(value) if value is not None else None
        )


@dataclass
@register("avg", "mean")
class Avg(Query):
    """Returns average of all items of given sequence."""
    
    path: Path | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get values
        if isinstance(self.path, Query):
            data = (self.path(item, *args, **kwargs) for item in data)
        
        # apply
        data = list(data)
        return sum(data) / len(data) if data else 0
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        value = next(iter(data.values()))
        
        # init instance
        return cls(
            path = Path.from_json(value) if value is not None else None
        )
