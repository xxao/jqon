# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from dataclasses import dataclass
from .errors import *
from .register import register
from .query import Query
from .expression import Expr


@dataclass
@register("take")
class Take(Query):
    """Takes number of items from sequence."""
    
    count: int | Expr | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get count
        count = self.count
        if isinstance(self.count, Query):
            count = self.count(data, *args, **kwargs)
        
        # get slice
        return data[:count]
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        count = next(iter(data.values()))
        
        # convert to expr
        if not isinstance(count, (int, type(None))):
            count = Expr.from_json(count)
        
        # init instance
        return cls(
            count = count
        )


@dataclass
@register("skip")
class Skip(Query):
    """Skips number of items from sequence."""
    
    count: int | Expr | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get count
        count = self.count
        if isinstance(self.count, Query):
            count = self.count(data, *args, **kwargs)
        
        # get slice
        return data[count:]
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        count = next(iter(data.values()))
        
        # convert to expr
        if not isinstance(count, (int, type(None))):
            count = Expr.from_json(count)
        
        # init instance
        return cls(
            count = count
        )


@dataclass
@register("slice")
class Slice(Query):
    """Takes slice of items from sequence."""
    
    start: int | Expr | None = None
    end: int | Expr | None = None
    step: int | Expr | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get start
        start = self.start
        if isinstance(self.start, Query):
            start = self.start(data, *args, **kwargs)
        
        # get end
        end = self.end
        if isinstance(self.end, Query):
            end = self.end(data, *args, **kwargs)
        
        # get step
        step = self.step
        if isinstance(self.step, Query):
            step = self.step(data, *args, **kwargs)
        
        # get slice
        return data[start:end:step]
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get values
        values = next(iter(data.values()))
        
        # check empty
        if values is None:
            return cls()
        
        # check values
        if not isinstance(values, list) or len(values) > 3:
            raise QSyntaxError("Slice definition must be a list of one, two or three values.")
        
        # get values
        start = values[0]
        end = values[1] if len(values) > 1 else None
        step = values[2] if len(values) > 2 else None
        
        # convert to expr
        if not isinstance(start, (int, type(None))):
            start = Expr.from_json(start)
        if not isinstance(end, (int, type(None))):
            end = Expr.from_json(end)
        if not isinstance(step, (int, type(None))):
            step = Expr.from_json(step)
        
        # init instance
        return cls(
            start = start,
            end = end,
            step = step
        )


@dataclass
@register("select")
class Select(Query):
    """Selects value from every item in sequence."""
    
    expr: Expr
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # select values
        return [self.expr(item, *args, **kwargs) for item in data]
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get values
        value = next(iter(data.values()))
        
        # convert to expr
        if value is not None:
            value = Expr.from_json(value)
        
        # init instance
        return cls(
            expr = value
        )


@dataclass
@register("many")
class Many(Query):
    """Flattens value from every item in sequence."""
    
    expr: Expr | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get values
        if isinstance(self.expr, Query):
            data = (self.expr(item, *args, **kwargs) for item in data)
        
        # flatten lists
        return [item for chain in data for item in chain]
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get values
        value = next(iter(data.values()))
        
        # convert to expr
        if value is not None:
            value = Expr.from_json(value)
        
        # init instance
        return cls(
            expr = value
        )


@dataclass
@register("where")
class Where(Query):
    """Gets items from sequence where condition met."""
    
    expr: Expr
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # filter items
        return [item for item in data if self.expr(item, *args, **kwargs)]
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        value = next(iter(data.values()))
        
        # init instance
        return cls(
            expr = Expr.from_json(value)
        )


@dataclass
@register("distinct")
class Distinct(Query):
    """Gets distinct items from sequence."""
    
    expr: Expr | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # check selector
        if not isinstance(self.expr, Query):
            return list(set(data))
        
        # find distinct
        seen = set()
        items = []
        for item in data:
            key = self.expr(item, *args, **kwargs)
            if key not in seen:
                seen.add(key)
                items.append(item)
        
        return items
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        value = next(iter(data.values()))
        
        # convert to expr
        if value is not None:
            value = Expr.from_json(value)
        
        # init instance
        return cls(
            expr = value
        )


@dataclass
@register("single")
class Single(Query):
    """Gets the single item from sequence where condition met."""
    
    expr: Expr | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get data
        if isinstance(self.expr, Query):
            data = (item for item in data if self.expr(item, *args, **kwargs))
        
        # use single
        i = -1
        item = None
        for i, item in enumerate(data):
            if i > 0:
                raise QIterError("More then one item found.")
        
        # found
        if i == 0:
            return item
        
        # no item found
        raise QIterError("No item found.")
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        value = next(iter(data.values()))
        
        # convert to expr
        if value is not None:
            value = Expr.from_json(value)
        
        # init instance
        return cls(
            expr = value
        )


@dataclass
@register("first")
class First(Single):
    """Gets the first item from sequence where condition met."""
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get data
        if isinstance(self.expr, Query):
            data = (item for item in data if self.expr(item, *args, **kwargs))
        
        # use first
        for item in data:
            return item
        
        # no item found
        raise QIterError("No item found.")


@dataclass
@register("last")
class Last(Single):
    """Gets the last item from sequence where condition met."""
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # get data
        data = reversed(data)
        if isinstance(self.expr, Query):
            data = (item for item in data if self.expr(item, *args, **kwargs))
        
        # use first
        for item in data:
            return item
        
        # no item found
        raise QIterError("No item found.")


@dataclass
@register("count")
class Count(Query):
    """Gets count of items in sequence where condition met."""
    
    expr: Expr | None = None
    
    
    def apply(self, data, *args, **kwargs):
        """Applies query to data."""
        
        # check selector
        if not isinstance(self.expr, Query):
            return len(data)
        
        # count true
        return sum(1 for item in data if self.expr(item, *args, **kwargs))
    
    
    @classmethod
    def from_json(cls, data):
        """Initialize instance from JSON."""
        
        # get value
        value = next(iter(data.values()))
        
        # convert to expr
        if value is not None:
            value = Expr.from_json(value)
        
        # init instance
        return cls(
            expr = value
        )
