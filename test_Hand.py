'''
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''

import unittest
from Hand import __init__

class TestHand(unittest.TestCase):
    def test_deck(self):
        # Test if Hand is legit
        self.assertRaises(TypeError,__init__,1)
        self.assertRaises(TypeError,__init__,True)
        self.assertRaises(TypeError,__init__,[1,'aa'])