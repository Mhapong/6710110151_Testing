from program.gridChallenge import gridChallenge
import unittest

class gridChallengeTest(unittest.TestCase):
    def test_gridChallenge_abc_lmp_qrt(self):
        expected = "YES"
        result = gridChallenge(["abc", "lmp", "qrt"])
        self.assertEqual(result, expected)

    def test_gridChallenge_mpxz_abcd_wcrt(self):
        expected = "NO"
        result = gridChallenge(["mpxz", "abcd", "wcrt"])
        self.assertEqual(result, expected)

    def test_gridChallenge_abcd(self):
        expected = "YES"
        result = gridChallenge(["abcd"])
        self.assertEqual(result, expected)

    def test_gridChallenge_a_b_c(self):
        expected = "YES"
        result = gridChallenge(["a", "b", "c"])
        self.assertEqual(result, expected)
    
    def test_gridChallenge_bac(self):
        expected = "NO"
        result = gridChallenge(['bac'])
        self.assertEqual(result,expected)
    
    def test_gridChallenge_abc_de(self):
        expected = "NO"
        result = gridChallenge(["abc", "de"])
        self.assertEqual(result,expected)   
        

    def test_gridChallenge_empty(self):
        expected = "YES"
        result = gridChallenge([])
        self.assertEqual(result, expected)
