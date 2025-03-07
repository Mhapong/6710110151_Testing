import unittest
from unittest.mock import patch
from function.random import guess_int, guess_float

class RandomTest(unittest.TestCase):
    
    @patch('random.randint', return_value=5)
    def test_guess_int_fixed_value(self, mock_randint):
        self.assertEqual(guess_int(1, 10), 5)
        mock_randint.assert_called_once_with(1, 10)
    
    @patch('random.randint', side_effect=[2, 7, 10])
    def test_guess_int_multiple_values(self, mock_randint):
        self.assertEqual(guess_int(1, 10), 2)
        self.assertEqual(guess_int(1, 10), 7)
        self.assertEqual(guess_int(1, 10), 10)
        self.assertEqual(mock_randint.call_count, 3)
    
    @patch('random.randint', return_value=1)
    def test_guess_int_lower_bound(self, mock_randint):
        self.assertEqual(guess_int(1, 10), 1)
    
    @patch('random.randint', return_value=10)
    def test_guess_int_upper_bound(self, mock_randint):
        self.assertEqual(guess_int(1, 10), 10)
    
    @patch('random.uniform', return_value=2.5)
    def test_guess_float_fixed_value(self, mock_uniform):
        self.assertEqual(guess_float(1.0, 3.0), 2.5)
        mock_uniform.assert_called_once_with(1.0, 3.0)
    
    @patch('random.uniform', side_effect=[1.1, 2.2, 3.3])
    def test_guess_float_multiple_values(self, mock_uniform):
        self.assertEqual(guess_float(1.0, 4.0), 1.1)
        self.assertEqual(guess_float(1.0, 4.0), 2.2)
        self.assertEqual(guess_float(1.0, 4.0), 3.3)
        self.assertEqual(mock_uniform.call_count, 3)
    
    @patch('random.uniform', return_value=1.0)
    def test_guess_float_lower_bound(self, mock_uniform):
        self.assertEqual(guess_float(1.0, 4.0), 1.0)
    
    @patch('random.uniform', return_value=4.0)
    def test_guess_float_upper_bound(self, mock_uniform):
        self.assertEqual(guess_float(1.0, 4.0), 4.0)