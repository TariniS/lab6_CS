#Name:Tarini Srikanth
#Instructor: Turner
#Project-Lab6-stirngs test


import unittest
from string_101 import *

class TestString(unittest.TestCase):
   def str_rot_13_test(self):
      self.assertEqual(str_rot_13('hello'),'uryyb')
   def str_rot_13_test2(self):
      self.assertEqual(str_rot_13('Tarini'),'Gnevav')
   def str_translate_101_test(self):
      self.assertEqual(str_translate_101('Tarini','i','n'),'Tarnnn')
   def str_transalte_test2(self):
      self.assertEqual(str_translate_101('Hello','l','i'),'Heiio')
      

if __name__ == '__main__':
   unittest.main()

