# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import unittest
import jqon as jq

try: from data import *
except: from .data import *


class TestCase(unittest.TestCase):
    """Test case for logical queries."""
    
    
    def test_and(self):
        """Tests AND condition."""
        
        text = """
            {"and": [
                {"<": ["$age", 20]},
                {">": ["$age", 5]}
            ]}
        """
        
        query = jq.from_text(text)
        self.assertTrue(query(P1))
        
        query = jq.from_text(text)
        self.assertFalse(query(P3))
    
    
    def test_or(self):
        """Tests OR condition."""
        
        text = """
            {"or": [
                {"<": ["$age", 20]},
                {">": ["$age", 60]}
            ]}
        """
        
        query = jq.from_text(text)
        self.assertTrue(query(P1))
        
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        
        query = jq.from_text(text)
        self.assertTrue(query(P4))
    
    
    def test_not(self):
        """Tests NOT condition."""
        
        # with queries
        text = """
            {"not": [
                {"<": ["$age", 20]},
                {">": ["$age", 100]}
            ]}
        """
        
        query = jq.from_text(text)
        self.assertFalse(query(P1))
        
        query = jq.from_text(text)
        self.assertTrue(query(P3))
    

# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
