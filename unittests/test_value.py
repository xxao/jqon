# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import unittest
import jqon as jq

try: from data import *
except: from .data import *


class TestCase(unittest.TestCase):
    """Test case for value query."""
    
    
    def test_number(self):
        """Tests number set and returned."""
        
        text = '{"value": 42}'
        query = jq.from_text(text)
        self.assertEqual(42, query('anything'))
    
    
    def test_string(self):
        """Tests string set and returned."""
        
        text = '{"value": "hello"}'
        query = jq.from_text(text)
        self.assertEqual("hello", query('anything'))
        
        text = '{"value": "$hello"}'
        query = jq.from_text(text)
        self.assertEqual("$hello", query('anything'))
    
    
    def test_list(self):
        """Tests list set and returned."""
        
        text = '{"value": [1, 2, 3]}'
        query = jq.from_text(text)
        self.assertEqual([1, 2, 3], query('anything'))
    
    
    def test_dict(self):
        """Tests dict set and returned."""
        
        text = '{"value": {"a": 1, "b": 2, "c": 3}}'
        query = jq.from_text(text)
        self.assertEqual({"a": 1, "b": 2, "c": 3}, query('anything'))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
