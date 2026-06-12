# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import unittest
import jqon as jq

try: from data import *
except: from .data import *


class TestCase(unittest.TestCase):
    """Test case for unary condition queries."""
    
    
    def test_true(self):
        """Tests true condition."""
        
        # test from data
        text = '{"true": null}'
        query = jq.from_text(text)
        self.assertTrue(query(1))
        self.assertFalse(query(0))
        
        # test from query
        text = '{"true": {"attr": "married"}}'
        query = jq.from_text(text)
        self.assertFalse(query(P1))
        self.assertTrue(query(P3))
        
        # test from expression
        text = '{"true": "$married"}'
        query = jq.from_text(text)
        self.assertFalse(query(P1))
        self.assertTrue(query(P3))
        
        # test from list
        text = '{"true": ["$married"]}'
        query = jq.from_text(text)
        self.assertFalse(query(P1))
        self.assertTrue(query(P3))
    
    
    def test_false(self):
        """Tests false condition."""
        
        # test from data
        text = '{"false": null}'
        query = jq.from_text(text)
        self.assertFalse(query(1))
        self.assertTrue(query(0))
        
        # test from query
        text = '{"false": {"attr": "married"}}'
        query = jq.from_text(text)
        self.assertTrue(query(P1))
        self.assertFalse(query(P3))
        
        # test from expression
        text = '{"false": "$married"}'
        query = jq.from_text(text)
        self.assertTrue(query(P1))
        self.assertFalse(query(P3))
        
        # test from expression
        text = '{"false": ["$married"]}'
        query = jq.from_text(text)
        self.assertTrue(query(P1))
        self.assertFalse(query(P3))
    
    
    def test_null(self):
        """Tests null condition."""
        
        # test from data
        text = '{"null": null}'
        query = jq.from_text(text)
        self.assertTrue(query(None))
        self.assertFalse(query(""))
        
        # test from query
        text = '{"null": {"attr": "items"}}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
        
        # test from expression
        text = '{"null": "$items"}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
        
        # test from expression
        text = '{"null": ["$items"]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
    
    
    def test_not_null(self):
        """Tests not null condition."""
        
        # test from data
        text = '{"not_null": null}'
        query = jq.from_text(text)
        self.assertFalse(query(None))
        self.assertTrue(query(""))
        
        # test from query
        text = '{"not_null": {"attr": "items"}}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
        
        # test from expression
        text = '{"not_null": "$items"}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
        
        # test from expression
        text = '{"not_null": ["$items"]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
    
    
    def test_empty(self):
        """Tests empty condition."""
        
        # test from data
        text = '{"empty": null}'
        query = jq.from_text(text)
        
        self.assertTrue(query(None))
        self.assertFalse(query(True))
        self.assertFalse(query(False))
        
        self.assertTrue(query(""))
        self.assertFalse(query("a"))
        
        self.assertFalse(query(0))
        self.assertFalse(query(1))
        
        self.assertTrue(query([]))
        self.assertFalse(query([1]))
        
        self.assertTrue(query(()))
        self.assertFalse(query((1,)))
        
        self.assertTrue(query({}))
        self.assertFalse(query({"a": 1}))
        self.assertFalse(query({1}))
        
        # test from query
        text = '{"empty": {"attr": "children"}}'
        query = jq.from_text(text)
        self.assertTrue(query(P1))
        self.assertFalse(query(P3))
        
        # test from expression
        text = '{"empty": "$children"}'
        query = jq.from_text(text)
        self.assertTrue(query(P1))
        self.assertFalse(query(P3))
    
    
    def test_not_empty(self):
        """Tests not empty condition."""
        
        # test empty
        text = '{"not_empty": null}'
        query = jq.from_text(text)
        
        self.assertFalse(query(None))
        self.assertTrue(query(True))
        self.assertTrue(query(False))
        
        self.assertFalse(query(""))
        self.assertTrue(query("a"))
        
        self.assertTrue(query(0))
        self.assertTrue(query(1))
        
        self.assertFalse(query([]))
        self.assertTrue(query([1]))
        
        self.assertFalse(query(()))
        self.assertTrue(query((1,)))
        
        self.assertFalse(query({}))
        self.assertTrue(query({"a": 1}))
        self.assertTrue(query({1}))
        
        # test from query
        text = '{"not_empty": {"attr": "children"}}'
        query = jq.from_text(text)
        self.assertFalse(query(P1))
        self.assertTrue(query(P3))
        
        # test from expression
        text = '{"not_empty": "$children"}'
        query = jq.from_text(text)
        self.assertFalse(query(P1))
        self.assertTrue(query(P3))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
