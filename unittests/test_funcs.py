# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import unittest
import jqon as jq

try: from data import *
except: from .data import *


class TestCase(unittest.TestCase):
    """Test case for function queries."""
    
    
    def test_bool(self):
        """Tests bool query."""
        
        # init selector
        text = '{"bool": null}'
        
        # test value
        query = jq.from_text(text)
        self.assertFalse(query(0))
        
        query = jq.from_text(text)
        self.assertTrue(query(1))
        
        # test collection
        query = jq.from_text(text)
        self.assertFalse(query([]))
        
        query = jq.from_text(text)
        self.assertTrue(query([1]))
    
    
    def test_len(self):
        """Tests len query."""
        
        # test from null
        text = '{"len": null}'
        query = jq.from_text(text)
        self.assertEqual(3, query([1, 2, 3]))
    
    
    def test_any(self):
        """Tests any query."""
        
        # test from null
        text = '{"any": null}'
        query = jq.from_text(text)
        self.assertTrue(query([P1.children, P3.children]))
        self.assertFalse(query([P1.children, P2.children]))
        
        # test from query
        text = '{"any": {"attr": "children"}}'
        query = jq.from_text(text)
        self.assertTrue(query([P1, P3]))
        self.assertFalse(query([P1, P2]))
        
        # test from expression
        text = '{"any": "$children"}'
        query = jq.from_text(text)
        self.assertTrue(query([P1, P3]))
        self.assertFalse(query([P1, P2]))
        
        # test from list
        text = '{"any": ["$children"]}'
        query = jq.from_text(text)
        self.assertTrue(query([P1, P3]))
        self.assertFalse(query([P1, P2]))
    
    
    def test_all(self):
        """Tests all query."""
        
        # test from null
        text = '{"all": null}'
        query = jq.from_text(text)
        self.assertTrue(query([P3.children, P4.children]))
        self.assertFalse(query([P1.children, P3.children]))
        
        # test from query
        text = '{"all": {"attr": "children"}}'
        query = jq.from_text(text)
        self.assertTrue(query([P3, P4]))
        self.assertFalse(query([P1, P3]))
        
        # test from expression
        text = '{"all": "$children"}'
        query = jq.from_text(text)
        self.assertTrue(query([P3, P4]))
        self.assertFalse(query([P1, P3]))
        
        # test from list
        text = '{"all": ["$children"]}'
        query = jq.from_text(text)
        self.assertTrue(query([P3, P4]))
        self.assertFalse(query([P1, P3]))
    
    
    def test_min(self):
        """Tests min query."""
        
        # init data
        data = [P1, P2, P3, P4]
        
        # test no kwy
        text = '{"min": null}'
        query = jq.from_text(text)
        self.assertEqual(1, query([2, 3, 1, 4]))
        
        # test key query
        text = '{"min": {"attr": "age"}}'
        query = jq.from_text(text)
        self.assertEqual(P2, query(data))
        
        # test key expression
        text = '{"min": "$age"}'
        query = jq.from_text(text)
        self.assertEqual(P2, query(data))
        
        # test from list
        text = '{"min": ["$age"]}'
        query = jq.from_text(text)
        self.assertEqual(P2, query(data))
    
    
    def test_max(self):
        """Tests max query."""
        
        # init data
        data = [P1, P2, P3, P4]
        
        # test from null
        text = '{"max": null}'
        query = jq.from_text(text)
        self.assertEqual(4, query([2, 3, 1, 4]))
        
        # test from query
        text = '{"max": {"attr": "age"}}'
        query = jq.from_text(text)
        self.assertEqual(P4, query(data))
        
        # test from expression
        text = '{"max": "$age"}'
        query = jq.from_text(text)
        self.assertEqual(P4, query(data))
        
        # test from list
        text = '{"max": ["$age"]}'
        query = jq.from_text(text)
        self.assertEqual(P4, query(data))
    
    
    def test_sum(self):
        """Tests sum query."""
        
        # init data
        data = [P1, P2, P3, P4]
        
        # test from null
        text = '{"sum": null}'
        query = jq.from_text(text)
        self.assertEqual(10, query([2, 3, 1, 4]))
        
        # test from query
        text = '{"sum": {"attr": "age"}}'
        query = jq.from_text(text)
        self.assertEqual(144, query(data))
        
        # test from expression
        text = '{"sum": "$age"}'
        query = jq.from_text(text)
        self.assertEqual(144, query(data))
        
        # test from list
        text = '{"sum": ["$age"]}'
        query = jq.from_text(text)
        self.assertEqual(144, query(data))
    
    
    def test_avg(self):
        """Tests avg query."""
        
        # init data
        data = [P1, P2, P3, P4]
        
        # test from null
        text = '{"avg": null}'
        query = jq.from_text(text)
        self.assertEqual(2.5, query([2, 3, 1, 4]))
        
        # test from query
        text = '{"avg": {"attr": "age"}}'
        query = jq.from_text(text)
        self.assertEqual(36, query(data))
        
        # test from expression
        text = '{"avg": "$age"}'
        query = jq.from_text(text)
        self.assertEqual(36, query(data))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
