from program.Staircase import Staircase
import unittest

class StaircaseTest(unittest.TestCase):
    def test_staircase_1(self):
        expected = "#"
        result = Staircase(1)
        self.assertEqual(result, expected)

    def test_staircase_2(self):
        expected = F" #\n##"
        result = Staircase(2)
        self.assertEqual(result, expected)

    def test_staircase_3(self):
        expected = "  #\n ##\n###"
        result = Staircase(3)
        self.assertEqual(result, expected)