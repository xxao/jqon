# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import unittest
import jqon as jq

try: from data import *
except: from .data import *


class TestCase(unittest.TestCase):
    """Test case for variable query."""
    
    
    def test_pass_through(self):
        """Tests data are passed through variable query."""
        
        # init data
        data = [P1, P2, P3]
        
        # test single
        text = '{"var": ["my_var", 42]}'
        query = jq.from_text(text)
        self.assertEqual(data, query(data))
        
        # test multiple
        text = """[
            {"var": ["my_var", 42]},
            {"item": 0},
            {"attr": "name"}
        ]
        """
        
        query = jq.from_text(text)
        self.assertEqual(data[0].name, query(data))
    
    
    def test_value(self):
        """Tests direct value accessible in subsequent queries."""
        
        # init data
        data = [P1, P2, P3]
        
        # test attr query
        text = """[
            {"var": ["my_var", 42]},
            {"attr": "my_var"}
        ]
        """
        
        query = jq.from_text(text)
        self.assertEqual(42, query(data))
        
        # test expr query
        text = """[
            {"var": ["my_var", 42]},
            {"expr": "$my_var"}
        ]
        """
        
        query = jq.from_text(text)
        self.assertEqual(42, query(data))
        
        # test condition
        text = """[
            {"var": ["my_var", 42]},
            {">": ["$my_var", 5]}
        ]
        """
        
        query = jq.from_text(text)
        self.assertTrue(query(data))
    
    
    def test_expr(self):
        """Tests expr value accessible in subsequent queries."""
        
        # init data
        data = [P1, P2, P3]
        
        # test attr query
        text = """[
            {"var": ["my_var", "$[2].age"]},
            {"attr": "my_var"}
        ]
        """
        
        query = jq.from_text(text)
        self.assertEqual(data[2].age, query(data))
        
        # test expr query
        text = """[
            {"var": ["my_var", "$[2].age"]},
            {"expr": "$my_var"}
        ]
        """
        
        query = jq.from_text(text)
        self.assertEqual(data[2].age, query(data))
        
        # test condition
        text = """[
            {"var": ["my_var", "$[2].age"]},
            {">": ["$my_var", 5]}
        ]
        """
        
        query = jq.from_text(text)
        self.assertTrue(query(data))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
