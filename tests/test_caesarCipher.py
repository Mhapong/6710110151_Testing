from function.caesarCipher import caesarCipher
import unittest

class caesarCipherTest(unittest.TestCase):
    def test_caesarCipher_lowercase(self):
        expected = "defghijklmnopqrstuvwxyzabc"
        result = caesarCipher("abcdefghijklmnopqrstuvwxyz",3)
        self.assertEqual(result, expected)
    
    def test_caesarCipher_uppercase(self):
        self.assertEqual(caesarCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3), "DEFGHIJKLMNOPQRSTUVWXYZABC")
    
    def test_caesarCipher_mixedcase(self):
        self.assertEqual(caesarCipher("HelloWorld", 5), "MjqqtBtwqi")
    
    def test_mixed_with_numbers_and_symbols(self):
        self.assertEqual(caesarCipher("123!@#Hello, World!", 3), "123!@#Khoor, Zruog!")
    
    def test_empty_string(self):
        self.assertEqual(caesarCipher("", 5), "")