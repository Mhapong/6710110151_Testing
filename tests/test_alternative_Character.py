from program.alternating_Characters import alternatingCharacters
import unittest

class alternatingCharactersTest(unittest.TestCase):
    def test_alternativeCharacters_ABABBA(self):
        expected = 1
        result = alternatingCharacters("ABABBA")
        self.assertEqual(result, expected)
    
    def test_alternativeCharacters_AAAAA(self):
        expected = 4
        result = alternatingCharacters("AAAAA")
        self.assertEqual(result, expected)
    
    def test_alternativeCharacters_ABABAB(self):
        expected = 0
        result = alternatingCharacters("ABABAB")
        self.assertEqual(result, expected)
    
    def test_alternativeCharacters_AAABBB(self):
        expected = 4  
        result = alternatingCharacters("AAABBB")
        self.assertEqual(result, expected)
    
    def test_alternativeCharacters_empty_string(self):
        expected = 0
        result = alternatingCharacters("")
        self.assertEqual(result, expected)
    
    
