import unittest
from Puzzle import Puzzle

class TestPuzzle(unittest.TestCase):

    def test_swap(self):
        p = Puzzle(['6', '7', 'x'], ['3', '1', '8'], ['2', '4', '5'])
        p.swap('7')
        self.assertEqual(p.rows, [['6', 'x', '7'], ['3', '1', '8'], ['2', '4', '5']])
        p.swap('1')
        self.assertEqual(p.rows, [['6', '1', '7'], ['3', 'x', '8'], ['2', '4', '5']])
        with self.assertRaises(ValueError):
            p.swap('5')

    def test_findNum(self):
        p = Puzzle(['6', '7', 'x'], ['3', '1', '8'], ['2', '4', '5'])
        self.assertEqual(p.findNum('3'), [1,0])
        self.assertEqual(p.findNum('4'), [2,1])
        self.assertEqual(p.findNum('x'), [0,2])

if __name__ == '__main__':
    unittest.main()
    # p = Puzzle(['2', '4', '6'], ['1', '3', 'x'], ['7', '5', '8'])
    # p.printPuzzle()
    # p.swap('8')
    # p.printPuzzle()