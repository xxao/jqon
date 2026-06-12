# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import unittest
import jqon as jq

try: from data import *
except: from .data import *


class TestCase(unittest.TestCase):
    """Test case for path query."""
    
    
    def test_single(self):
        """Tests single query init."""
        
        # init data
        data = P1
        
        # test from Path
        text = '{"attr": "age"}'
        query = jq.Path.from_text(text)
        self.assertEqual(data.age, query(data))
        
        # test from Query
        text = f'{{"path": {text}}}'
        query = jq.Query.from_text(text)
        self.assertEqual(data.age, query(data))
    
    
    def test_multi(self):
        """Tests multi query init."""
        
        # init data
        data = P1
        
        # test list
        text = """[
            {"attr": "address"},
            {"attr": "city"}
        ]
        """
        
        query = jq.Path.from_text(text)
        self.assertEqual(data.address.city, query(data))
        
        query = jq.Query.from_text(text)
        self.assertEqual(data.address.city, query(data))
        
        # test dict
        text = f'{{"path": {text}}}'
        query = jq.Query.from_text(text)
        self.assertEqual(data.address.city, query(data))
    
    
    def test_attr(self):
        """Tests attr selector."""
        
        # init data
        data = P1
        
        # test simple
        text = "$age"
        query = jq.Path.from_json(text)
        self.assertEqual(data.age, query(data))
        
        text = f'{{"path": "{text}"}}'
        query = jq.Query.from_text(text)
        self.assertEqual(data.age, query(data))
        
        # test chain
        text = "$address.city"
        query = jq.Path.from_json(text)
        self.assertEqual(data.address.city, query(data))
        
        # test from query
        text = f'{{"path": "{text}"}}'
        query = jq.Query.from_text(text)
        self.assertEqual(data.address.city, query(data))
    
    
    def test_call(self):
        """Tests call selector."""
        
        # test simple
        text = "$len()"
        data = P3.children
        query = jq.Path.from_json(text)
        self.assertEqual(len(data), query(data))
        
        text = f'{{"path": "{text}"}}'
        query = jq.Query.from_text(text)
        self.assertEqual(len(data), query(data))
        
        # test chain
        text = "$children.len()"
        data = P3
        query = jq.Path.from_json(text)
        self.assertEqual(len(data.children), query(data))
        
        text = f'{{"path": "{text}"}}'
        query = jq.Query.from_text(text)
        self.assertEqual(len(data.children), query(data))
    
    
    def test_index(self):
        """Tests index selector."""
        
        # test simple
        text = "$[1]"
        data = P3.children
        query = jq.Path.from_json(text)
        self.assertEqual(data[1], query(data))
        
        text = f'{{"path": "{text}"}}'
        query = jq.Query.from_text(text)
        self.assertEqual(data[1], query(data))
        
        # test attr
        text = "$children[1]"
        data = P3
        query = jq.Path.from_json(text)
        self.assertEqual(data.children[1], query(data))
        
        text = f'{{"path": "{text}"}}'
        query = jq.Query.from_text(text)
        self.assertEqual(data.children[1], query(data))
    
    
    def test_item(self):
        """Tests item selector."""
        
        # test simple
        text = "$[lego]"
        data = P1.items
        query = jq.Path.from_json(text)
        self.assertEqual(data["lego"], query(data))
        
        text = f'{{"path": "{text}"}}'
        query = jq.Query.from_text(text)
        self.assertEqual(data["lego"], query(data))
        
        # test attr
        text = "$items[lego]"
        data = P1
        query = jq.Path.from_json(text)
        self.assertEqual(data.items["lego"], query(data))
        
        text = f'{{"path": "{text}"}}'
        query = jq.Query.from_text(text)
        self.assertEqual(data.items["lego"], query(data))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
