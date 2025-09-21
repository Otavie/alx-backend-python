#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map function 
Unit test for utils.get_json function 
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json

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
    
class TestGetJson(unittest.TestCase):
    """Test class for get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected payload from a mocked requests.get"""
        # Create a mock response with .json() method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        
        result = get_json(test_url)
        
        # Assert requests.get was called once with the test URL
        mock_get.assert_called_once_with(test_url)
        
        # Assert the result of get_json is the expected payload
        self.assertEqual(result, test_payload)
    