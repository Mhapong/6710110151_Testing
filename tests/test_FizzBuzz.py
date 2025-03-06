from function.FizzBuzz import FizzBuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz_3(self):
        result = FizzBuzz(3)
        self.assertEqual(result, "Fizz")

    def test_fizzbuzz_5(self):
        result = FizzBuzz(5)
        self.assertEqual(result, "Buzz")

    def test_fizzbuzz_45(self):
        result = FizzBuzz(45)
        self.assertEqual(result, "FizzBuzz")

    def test_fizzbuzz_1(self):
        result = FizzBuzz(1)
        self.assertEqual(result, 1)
