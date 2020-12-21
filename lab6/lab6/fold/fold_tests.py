#Name:Tarini Srikanth
#Instructor: Clark Turner
#Project- Lab 6- Folds Test


import unittest
from fold import *

class TestCases(unittest.TestCase):
   def test_sum(self):
      Inputlist=[1,2,3,4,5]
      self.assertEqual(sum(Inputlist),15)
   def test_sum2(self):
      inputList2=[2,3,4,5,6]
      self.assertEqual(sum(inputList2),20)
   def test_index_of_smallest(self):
      inputList =[1,2,3,4,5]
      self.assertEqual(index_of_smallest(inputList),0)
   def test_index_2(self):
      inputList2= [3,4,5,6,-1]
      self.assertEqual(index_of_smallest(inputList2),4)
   def test_index_3(self):
      inputList3=[4,5,3,3,6,7]
      self.assertEqual(index_of_smallest(inputList3),2)
      
      
      


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

