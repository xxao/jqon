# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import unittest
import jqon as jq

try: from data import *
except: from .data import *


class TestCase(unittest.TestCase):
    """Test case for enumerable queries."""
    
    
    def test_take(self):
        """Tests take query."""
        
        # init data
        data = [P1, P2, P3, P4]
        
        # test from null
        text = '{"take": null}'
        query = jq.from_text(text)
        self.assertEqual(data[:], query(data))
        
        # test from value
        text = '{"take": 2}'
        query = jq.from_text(text)
        self.assertEqual(data[:2], query(data))
        
        # test from query
        text = '{"take": {"value": 2}}'
        query = jq.from_text(text)
        self.assertEqual(data[:2], query(data))
        
        # test from expression
        text = '{"take": "$[0].items[merkur]"}'
        query = jq.from_text(text)
        self.assertEqual(data[:2], query(data))
        
        # test from list
        text = '{"take": ["$[0]", "$items[merkur]"]}'
        query = jq.from_text(text)
        self.assertEqual(data[:2], query(data))
    
    
    def test_skip(self):
        """Tests skip query."""
        
        # init data
        data = [P1, P2, P3, P4]
        
        # test from null
        text = '{"skip": null}'
        query = jq.from_text(text)
        self.assertEqual(data[:], query(data))
        
        # test from value
        text = '{"skip": 2}'
        query = jq.from_text(text)
        self.assertEqual(data[2:], query(data))
        
        # test from query
        text = '{"skip": {"value": 2}}'
        query = jq.from_text(text)
        self.assertEqual(data[2:], query(data))
        
        # test from expression
        text = '{"skip": "$[0].items[merkur]"}'
        query = jq.from_text(text)
        self.assertEqual(data[2:], query(data))
        
        # test from expression
        text = '{"skip": ["$[0]", "$items[merkur]"]}'
        query = jq.from_text(text)
        self.assertEqual(data[2:], query(data))
    
    
    def test_slice(self):
        """Tests slice query."""
        
        # init data
        data = [P1, P2, P3, P4]
        
        # test from null
        text = '{"slice": null}'
        query = jq.from_text(text)
        self.assertEqual(data[:], query(data))
        
        # test from value
        text = '{"slice": [2]}'
        query = jq.from_text(text)
        self.assertEqual(data[2:], query(data))
        
        text = '{"slice": [null]}'
        query = jq.from_text(text)
        self.assertEqual(data[:], query(data))
        
        text = '{"slice": [1, 2]}'
        query = jq.from_text(text)
        self.assertEqual(data[1:2], query(data))
        
        text = '{"slice": [null, 2]}'
        query = jq.from_text(text)
        self.assertEqual(data[:2], query(data))
        
        text = '{"slice": [1, 2, 2]}'
        query = jq.from_text(text)
        self.assertEqual(data[1:2:2], query(data))
        
        text = '{"slice": [null, null, 2]}'
        query = jq.from_text(text)
        self.assertEqual(data[::2], query(data))
        
        # test from query
        text = '{"slice": [{"value": 1}, {"value": 2}, {"value": 2}]}'
        query = jq.from_text(text)
        self.assertEqual(data[1:2:2], query(data))
        
        # test from expression
        text = '{"slice": ["$[0].items[bike]", "$[0].items[merkur]", "$[0].items[merkur]"]}'
        query = jq.from_text(text)
        self.assertEqual(data[1:2:2], query(data))
        
        # test from lists
        text = '{"slice": [["$[0]", "$items[bike]"], ["$[0]", "$items[merkur]"], ["$[0]", "$items[merkur]"]]}'
        query = jq.from_text(text)
        self.assertEqual(data[1:2:2], query(data))
    
    
    def test_select(self):
        """Tests select query."""
        
        # init data
        data = [P1, P2, P3, P4]
        
        # test from query
        text = '{"select": {"attr": "name"}}'
        query = jq.from_text(text)
        self.assertEqual([p.name for p in data], query(data))
        
        # test from expression
        text = '{"select": "$name"}'
        query = jq.from_text(text)
        self.assertEqual([p.name for p in data], query(data))
        
        # test from list
        text = '{"select": ["$address", "$country"]}'
        query = jq.from_text(text)
        self.assertEqual([p.address.country for p in data], query(data))
    
    
    def test_many(self):
        """Tests many query."""
        
        # test from null
        text = '{"many": null}'
        query = jq.from_text(text)
        data = [P1.children, P2.children, P3.children, P4.children]
        self.assertEqual([c for p in data for c in p], query(data))
        
        # test from query
        text = '{"many": {"attr": "children"}}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual([c for p in data for c in p.children], query(data))
        
        # test from expression
        text = '{"many": "$children"}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual([c for p in data for c in p.children], query(data))
        
        # test from list
        text = '{"many": ["$children"]}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual([c for p in data for c in p.children], query(data))
    
    
    def test_where(self):
        """Tests where query."""
        
        # init data
        data = [P1, P2, P3, P4]
        
        # test from query
        text = '{"where": {"attr": "children"}}'
        query = jq.from_text(text)
        self.assertEqual([p for p in data if p.children], query(data))
        
        # test from expression
        text = '{"where": "$children"}'
        query = jq.from_text(text)
        self.assertEqual([p for p in data if p.children], query(data))
        
        # test from queries
        text = """
            {"where": [
                {"not_empty": "$children"}
            ]}
        """
        query = jq.from_text(text)
        self.assertEqual([p for p in data if p.children], query(data))
    
    
    def test_distinct(self):
        """Tests distinct query."""
        
        # test from null
        text = '{"distinct": null}'
        data = [0, 1, 2, 3, 1, 2, 5]
        query = jq.from_text(text)
        self.assertEqual(set(data), set(query(data)))
        
        # test from query
        text = '{"distinct": {"attr": "married"}}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual([P1, P3], query(data))
        
        # test from expression
        text = '{"distinct": "$address.country"}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual([P1, P4], query(data))
        
        # test from list
        text = '{"distinct": ["$address", "$country"]}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual([P1, P4], query(data))
    
    
    def test_first(self):
        """Tests first query."""
        
        # test from null
        text = '{"first": null}'
        data = [0, 1, 2, 3, 1, 2, 5]
        query = jq.from_text(text)
        self.assertEqual(0, query(data))
        
        # test from query
        text = '{"first": {">": ["$age", 20]}}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual(P3, query(data))
        
        # test from expression
        text = '{"first": "$married"}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual(P3, query(data))
        
        # test from list
        text = '{"first": ["$children", "$len()"]}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual(P3, query(data))
    
    
    def test_last(self):
        """Tests last query."""
        
        # test from null
        text = '{"last": null}'
        data = [0, 1, 2, 3, 1, 2, 5]
        query = jq.from_text(text)
        self.assertEqual(5, query(data))
        
        # test from query
        text = '{"last": {"<": ["$age", 10]}}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual(P2, query(data))
        
        # test from expression
        text = '{"last": "$married"}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual(P4, query(data))
        
        # test from list
        text = '{"last": ["$children", "$len()"]}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual(P4, query(data))
    
    
    def test_single(self):
        """Tests single query."""
        
        # test from null
        text = '{"single": null}'
        data = [0]
        query = jq.from_text(text)
        self.assertEqual(0, query(data))
        
        # test from query
        text = '{"single": {">": ["$age", 60]}}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual(P4, query(data))
        
        # test from list
        text = '{"single": [{">": ["$age", 60]}]}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual(P4, query(data))
    
    
    def test_count(self):
        """Tests count query."""
        
        # test from null
        text = '{"count": null}'
        data = [0, 1, 2, 3, 1, 2, 5]
        query = jq.from_text(text)
        self.assertEqual(7, query(data))
        
        # test from query
        text = '{"count": {">": ["$age", 10]}}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual(2, query(data))
        
        # test from expression
        text = '{"count": "$married"}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual(2, query(data))
        
        # test from expression
        text = '{"count": ["$children", "$len()"]}'
        query = jq.from_text(text)
        data = [P1, P2, P3, P4]
        self.assertEqual(2, query(data))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
