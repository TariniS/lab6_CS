#Name: Tarini Srikanth
#Instrcutor: Clark Turner
#Project- Lab 6 Char tests


import unittest
from char import *

class TestChar(unittest.TestCase):
   def test_lower(self):
      self.assertEqual(is_lower_01('a'),True)
   def test_lower2(self):
      self.assertEqual(is_lower_01('A'),False)
   def test_rot13(self):
      self.assertEqual(char_rot_13('b'),'o')
   def test_rot_13(self):
      self.assertEqual(char_rot_13('N'),'A')
   


if __name__ == '__main__':
   unittest.main()

