import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../src')))

from src.outfit_recommender import recommend_outfit

class TestOutfitRecommender(unittest.TestCase):
    def test_recommend_outfit(self):
        self.assertEqual(recommend_outfit(30,"Sunny"),"T-shirt,jeans")
        self.assertEqual(recommend_outfit(20,"Cloudy"),"Jacket,jeans")
        self.assertEqual(recommend_outfit(10,"Rainy"),"Jacket,jeans")
        self.assertEqual(recommend_outfit(0,"Snowy"),"Heavy coat, woolen scarf")

if __name__ == "__main__":
    unittest.main()