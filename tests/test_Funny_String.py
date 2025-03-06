from program.funnyString import funnyString
import unittest

class funnyStringTest(unittest.TestCase):
    def test_funny_string_normal_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_funny_string_normal_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")