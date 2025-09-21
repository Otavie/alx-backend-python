#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map function 
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function"""
    
    @parameterized.expand([
        # Test Case 1: Simple one-level nested map
        ({"a": 1}, ("a", ), 1),
        # Test Case 2: Two-level nested map, accessing first level
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        #Test Case 3: Two-level nested map, accessing second level
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    
    def test_access_nested_map(self, nested_map, path, expected_result):
        # Assert that function returns expected result for given inputs
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
        
    @parameterized.expand([
        ({}, ("b",), "b"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Test that access_nested_map raises KeyError for invalid paths"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_key}'")
    
