# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import unittest
import jqon as jq

try: from data import *
except: from .data import *


class TestCase(unittest.TestCase):
    """Test case for getter queries."""
    
    
    def test_attr(self):
        """Tests attribute selector."""
        
        # test direct
        text = '{"attr": "age"}'
        data = P1
        query = jq.from_text(text)
        self.assertEqual(data.age, query(data))
    
    
    def test_item(self):
        """Tests item selector."""
        
        # test list
        text = '{"item": 2}'
        data = [0, 1, 2, 3]
        query = jq.from_text(text)
        self.assertEqual(data[2], query(data))
        
        # test dict
        text = '{"item": "b"}'
        data = {"a": 0, "b": 1, "c": 2, "d": 3}
        query = jq.from_text(text)
        self.assertEqual(data["b"], query(data))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
