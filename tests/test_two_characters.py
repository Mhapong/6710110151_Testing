from function.two_characters import alternate
import unittest

class AlternateCharactersTest(unittest.TestCase):
    def test_alternate_wasdwasd(self):
        expected = 4
        result = alternate("wasdwasd")
        self.assertEqual(result, expected)
    
    def test_alternate_asdasd(self):
        expected = 4
        result = alternate("asdasd")
        self.assertEqual(result, expected)
    
    def test_alternate_no_cCcCCc(self):
        expected = 0
        result = alternate("cCcCCc")
        self.assertEqual(result, expected)
    
    def test_alternate_beabeefeab(self):
        expected = 5
        result = alternate("beabeefeab")
        self.assertEqual(result, expected)

