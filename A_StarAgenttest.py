import unittest
from Puzzle import Puzzle
from A_Star_SolvingAgent import SolvingAgent

class TestAStarAgent(unittest.TestCase):

    def test_solvePuzzle(self):
        p = Puzzle(['5', '4', '3'], ['2', '1', '0'], ['6', '7', '8'])
        self.assertEqual(SolvingAgent(p, '1').solvePuzzle(), \
            ['1', '2', '5', '4', '3', '1', '2', '5', '4', '3', '1', '2', '5', '4', '3'])
        self.assertEqual(SolvingAgent(p, '2').solvePuzzle(), \
            ['1', '2', '5', '4', '3', '1', '2', '5', '4', '3', '1', '2', '5', '4', '3'])
            
        p = Puzzle(['8', '7', '6'], ['5', '4', '3'], ['2', '1', '0'])
        self.assertEqual(SolvingAgent(p, '1').solvePuzzle(), \
            ['1', '2', '5', '8', '7', '6', '3', '1', '2', '5', '8', '7', '6', '3', '1', \
                '2', '5', '8', '7', '6', '3', '1', '2', '5', '8', '7', '6', '3'])
        self.assertEqual(SolvingAgent(p, '2').solvePuzzle(), \
            ['1', '2', '5', '8', '7', '6', '3', '1', '2', '5', '8', '7', '6', '3', '1', \
                '2', '5', '8', '7', '6', '3', '1', '2', '5', '8', '7', '6', '3'])

if __name__ == '__main__':
    unittest.main()