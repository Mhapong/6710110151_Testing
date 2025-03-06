from program.Cat_and_Mouse import catAndMouse
import unittest

class catAndMouseTest(unittest.TestCase):
    def test_cat_and_mouse_1_2_3(self):
        expected = "Cat B"
        result = catAndMouse(1,2,3)
        self.assertEqual(result, expected)
    def test_cat_and_mouse_1_3_2(self):
        expected = "Mouse C"
        result = catAndMouse(1,3,2)
        self.assertEqual(result, expected)
    def test_cat_and_mouse_1_5_2(self):
        expected = "Cat A"
        result = catAndMouse(1,5,2)
        self.assertEqual(result, expected)