# test_blockapi.py
"""
Tests for BlockAPI module.
"""

import unittest
from blockapi import BlockAPI

class TestBlockAPI(unittest.TestCase):
    """Test cases for BlockAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockAPI()
        self.assertIsInstance(instance, BlockAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
