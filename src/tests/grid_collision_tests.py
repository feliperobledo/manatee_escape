import unittest
from src.grid_collisions import get_next_state_map

class TestBoatCollision(unittest.TestCase):

    def test_boat_moves(self):
        # given
        map_input = [[" ", "B"],
                     [" ", " "]]
        # when
        get_next_state_map(map_input, [])

        # then
        expect = [[" ", " "],
                  [" ", "B"]]

        self.assertEqual(expect, map_input)

    def test_rock_stops_boat(self):
        # given
        map_input = [[" ", "B"],
                     [" ", "R"]]
        # when
        get_next_state_map(map_input, [])

        # then
        expect = [[" ", "B"],
                  [" ", "R"]]

        self.assertEqual(expect, map_input)

    def test_boat_stays_in_bounds(self):
        # given
        map_input = [[" ", "B"],
                     ["B", "B"]]
        # when
        get_next_state_map(map_input, [])

        # then
        expect = [[" ", "B"],
                  ["B", "B"]]


        self.assertEqual(expect, map_input)

    def test_boat_moves_left(self):
        # given
        map_input = [[" ", "B", " "],
                     [" ", "B", " "]]
        # when
        get_next_state_map(map_input, [])

        # then
        expect = [[" ", " ", " "],
                  ["B", "B", " "]]

        self.assertEqual(expect, map_input)

    def test_boat_moves_right(self):
        # given
        map_input = [[" ", "B", " "],
                     ["B", "B", " "]]
        # when
        get_next_state_map(map_input, [])

        # then
        expect = [[" ", " ", " "],
                  ["B", "B", "B"]]

        self.assertEqual(expect, map_input)

    def test_boats_move_in_order_right(self):
        # given
        map_input = [[' ', 'B', 'B', 'B'],
                     ['B', 'B', ' ', ' ']]

        # when
        get_next_state_map(map_input, [])

        # then
        expect = [[' ', ' ', ' ', 'B'],
                  ['B', 'B', 'B', 'B']]


        self.assertEqual(expect, map_input)

    def test_boats_move_in_order_left(self):
        # given
        map_input = [['B', 'B', 'B', ' '],
                     [' ', ' ', 'B', 'B']]

        # when
        get_next_state_map(map_input, [])

        # then
        expect = [[' ', ' ', 'B', ' '],
                  ['B', 'B', 'B', 'B']]


        self.assertEqual(expect, map_input)
