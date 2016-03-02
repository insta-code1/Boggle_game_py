import unittest
import boggle
from random import choice
from string import ascii_uppercase

class TestThatStuffWorks(unittest.TestCase):

    def Test_grid_coordinates(self):
        grid = boggle.get_grid()
        self.assertTrue((0, 0) in grid)
        self.assertTrue((1, 0) in grid)
        self.assertTrue((0, 1) in grid)
        self.assertTrue((1, 1) in grid)

    def