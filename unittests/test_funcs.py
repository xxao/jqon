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


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
