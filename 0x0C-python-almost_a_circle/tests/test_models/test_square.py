#!/usr/bin/python3
"""Unit test class Square"""
from models.square import Square
import sys
from io import StringIO
def test_to_dictionary(self):
    s1 = Square(10, 2, 1, 9)
    s1_dict = s1.to_dictionary()
    expected = {'id': 9, 'size': 10, 'x': 2, 'y': 1}
    self.assertEqual(s1_dict, expected)

