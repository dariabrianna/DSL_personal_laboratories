from lab5 import Grammar
import unittest

class TestGrammar(unittest.TestCase):
    def setUp(self):
        self.g = Grammar()
        self.P1, self.P2, self.P3, self.P4, self.P5 = self.g.ReturnProductions()

    def test_remove_epsilon(self):
        # Test RemoveEpsilon method
        expected_result = {'S': ['bA', 'BC', 'A', 'bS', 'bCAa', 'bAa'], 'A': ['a', 'aS', 'bCaCa', 'baa', 'baa'], 'B': ['bS', 'bCAa', 'bAa', 'a', 'aS', 'bCaCa', 'baa', 'baa'], 'C': ['AB'], 'D': ['AB']}


        self.assertEqual(self.P1, expected_result)
    
    def test_eliminate_unit_prod(self):
        # Test EliminateUnitProd method
        expected_result = {'S': ['bA', 'BC', 'A', 'bS', 'bCAa', 'bAa'], 'A': ['a', 'aS', 'bCaCa', 'baa', 'baa'], 'B': ['bS', 'bCAa', 'bAa', 'a', 'aS', 'bCaCa', 'baa', 'baa'], 'C': ['AB'], 'D': ['AB']}
        self.assertEqual(self.P2, expected_result)

    def test_eliminate_inaccesible(self):
        # Test EliminateInaccesible method
        expected_result = {'S': ['bA', 'BC', 'A', 'bS', 'bCAa', 'bAa'], 'A': ['a', 'aS', 'bCaCa', 'baa', 'baa'], 'B': ['bS', 'bCAa', 'bAa', 'a', 'aS', 'bCaCa', 'baa', 'baa'], 'C': ['AB']}
        self.assertEqual(self.P3, expected_result)

    def test_remove_unprod(self):
        # Test RemoveUnprod method
        expected_result = {'S': ['bA', 'BC', 'A', 'bS', 'bCAa', 'bAa'], 'A': ['a', 'aS', 'bCaCa', 'baa', 'baa'], 'B': ['bS', 'bCAa', 'bAa', 'a', 'aS', 'bCaCa', 'baa', 'baa'], 'C': ['AB']}
        self.assertEqual(self.P4, expected_result)

    def test_obtain_cnf(self):
        # Test ObtainCNF method
        expected_result = {'S': ['DE', 'BC', 'FE', 'DG', 'HI', 'DI'], 'A': ['a', 'JG', 'HK', 'DL', 'DL'], 'B': ['DG', 'HI', 'DI', 'a', 'JG', 'HK', 'DL', 'DL'], 'C': ['AB'], 'D': ['b'], 'E': ['A'], 'F': [''], 'G': ['S'], 'H': ['bC'], 'I': ['Aa'], 'J': ['a'], 'K': ['aCa'], 'L': ['aa']}
        self.assertEqual(self.P5, expected_result)

if __name__ == '__main__':
    unittest.main()