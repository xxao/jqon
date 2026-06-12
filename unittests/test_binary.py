# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import unittest
import jqon as jq

try: from data import *
except: from .data import *


class TestCase(unittest.TestCase):
    """Test case for binary condition queries."""
    
    
    def test_equal(self):
        """Tests equal condition."""
        
        # test left from data
        text = '{"==": 50}'
        query = jq.from_text(text)
        self.assertTrue(query(50))
        self.assertFalse(query(20))
        
        text = '{"==": "text"}'
        query = jq.from_text(text)
        self.assertTrue(query("text"))
        self.assertFalse(query("TEXT"))
        
        # test left from query
        text = '{"==": [{"attr": "age"}, 50]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
        
        text = '{"==": [{"attr": "name"}, "P3"]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
        
        # test left from expression
        text = '{"==": ["$age", 50]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
        
        text = '{"==": ["$name", "P3"]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
        
        # test right from query
        text = '{"==": {"value": 50}}'
        query = jq.from_text(text)
        self.assertTrue(query(50))
        self.assertFalse(query(20))
        
        text = '{"==": {"value": "text"}}'
        query = jq.from_text(text)
        self.assertTrue(query("text"))
        self.assertFalse(query("TEXT"))
        
        # test both from query
        text = '{"==": [{"attr": "age"}, {"value": 50}]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
        
        text = '{"==": [{"attr": "name"}, {"value": "P3"}]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
    
    
    def test_not_equal(self):
        """Tests not equal condition."""
        
        # test left from data
        text = '{"!=": 50}'
        query = jq.from_text(text)
        self.assertFalse(query(50))
        self.assertTrue(query(20))
        
        # test left from query
        text = '{"!=": [{"attr": "age"}, 50]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
        
        # test left from expression
        text = '{"!=": ["$age", 50]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
        
        # test right from query
        text = '{"!=": {"value": 50}}'
        query = jq.from_text(text)
        self.assertFalse(query(50))
        self.assertTrue(query(20))
        
        # test both from query
        text = '{"!=": [{"attr": "age"}, {"value": 50}]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
    
    
    def test_greater(self):
        """Tests greater condition."""
        
        # test left from data
        text = '{">": 20}'
        query = jq.from_text(text)
        self.assertTrue(query(50))
        self.assertFalse(query(20))
        
        # test left from query
        text = '{">": [{"attr": "age"}, 20]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
        
        # test left from expression
        text = '{">": ["$age", 20]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
        
        # test right from query
        text = '{">": {"value": 20}}'
        query = jq.from_text(text)
        self.assertTrue(query(50))
        self.assertFalse(query(20))
        
        # test both from query
        text = '{">": [{"attr": "age"}, {"value": 20}]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
    
    
    def test_greater_or_equal(self):
        """Tests greater or equal condition."""
        
        # test left from data
        text = '{">=": 10}'
        query = jq.from_text(text)
        self.assertTrue(query(50))
        self.assertTrue(query(10))
        self.assertFalse(query(7))
        
        # test left from query
        text = '{">=": [{"attr": "age"}, 10]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertTrue(query(P1))
        self.assertFalse(query(P2))
        
        # test left from expression
        text = '{">=": ["$age", 10]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertTrue(query(P1))
        self.assertFalse(query(P2))
        
        # test right from query
        text = '{">=": {"value": 10}}'
        query = jq.from_text(text)
        self.assertTrue(query(50))
        self.assertTrue(query(10))
        self.assertFalse(query(7))
        
        # test both from query
        text = '{">=": [{"attr": "age"}, {"value": 10}]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertTrue(query(P1))
        self.assertFalse(query(P2))
    
    
    def test_less(self):
        """Tests less condition."""
        
        # test left from data
        text = '{"<": 50}'
        query = jq.from_text(text)
        self.assertFalse(query(50))
        self.assertTrue(query(20))
        
        # test left from query
        text = '{"<": [{"attr": "age"}, 50]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
        
        # test left from expression
        text = '{"<": ["$age", 50]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
        
        # test right from query
        text = '{"<": {"value": 50}}'
        query = jq.from_text(text)
        self.assertFalse(query(50))
        self.assertTrue(query(20))
        
        # test both from query
        text = '{"<": [{"attr": "age"}, {"value": 50}]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
    
    
    def test_less_or_equal(self):
        """Tests less or equal condition."""
        
        # test left from data
        text = '{"<=": 10}'
        query = jq.from_text(text)
        self.assertFalse(query(50))
        self.assertTrue(query(10))
        self.assertTrue(query(7))
        
        # test left from query
        text = '{"<=": [{"attr": "age"}, 10]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
        self.assertTrue(query(P2))
        
        # test left from expression
        text = '{"<=": ["$age", 10]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
        self.assertTrue(query(P2))
        
        # test right from query
        text = '{"<=": {"value": 10}}'
        query = jq.from_text(text)
        self.assertFalse(query(50))
        self.assertTrue(query(10))
        self.assertTrue(query(7))
        
        # test both from query
        text = '{"<=": [{"attr": "age"}, {"value": 10}]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
        self.assertTrue(query(P2))
    
    
    def test_in(self):
        """Tests in condition."""
        
        # test from data
        text = '{"in": {"value": [10, 20, 30]}}'
        query = jq.from_text(text)
        self.assertFalse(query(50))
        self.assertTrue(query(20))
        
        # test from query
        text = '{"in": [{"attr": "age"}, {"value": [10, 20, 30]}]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
        
        # test from expression
        text = '{"in": ["$age", {"value": [10, 20, 30]}]}'
        query = jq.from_text(text)
        self.assertFalse(query(P3))
        self.assertTrue(query(P1))
    
    
    def test_not_in(self):
        """Tests not in condition."""
        
        # test from data
        text = '{"not_in": {"value": [10, 20, 30]}}'
        query = jq.from_text(text)
        self.assertTrue(query(50))
        self.assertFalse(query(20))
        
        # test from query
        text = '{"not_in": [{"attr": "age"}, {"value": [10, 20, 30]}]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
        
        # test from expression
        text = '{"not_in": ["$age", {"value": [10, 20, 30]}]}'
        query = jq.from_text(text)
        self.assertTrue(query(P3))
        self.assertFalse(query(P1))
    
    
    def test_contains(self):
        """Tests contains condition."""
        
        # test from data
        text = '{"contains": 10}'
        query = jq.from_text(text)
        self.assertTrue(query([10, 20, 30]))
        self.assertFalse(query([20, 30]))
        
        # test from query
        text = '{"contains": [{"attr": "items"}, "merkur"]}'
        query = jq.from_text(text)
        self.assertTrue(query(P1))
        self.assertFalse(query(P2))
        
        # test from expression
        text = '{"contains": ["$items", "merkur"]}'
        query = jq.from_text(text)
        self.assertTrue(query(P1))
        self.assertFalse(query(P2))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
