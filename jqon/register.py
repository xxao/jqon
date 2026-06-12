# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

# define available queries
QUERIES = {}


def register(*tags):
    """Registers query by given tag."""
    
    
    def reg(cls):
        """Registers given class."""
        
        for tag in tags:
            QUERIES[tag] = cls
        return cls
    
    return reg
