import unittest
from ..models.map import Map
from ..common.map_data import map_data
from ..common.enums import Terrain

class Test_Map(unittest.TestCase):
    def setUp(self):
        self.map = Map(map_data)

    def test_map_returns_terrain_for_hex(self):
        """ Tests that the right terrain is returned when a hex is called. """
        terrain = self.map.get_terrain((2,2))
        assert terrain == Terrain.FOREST
        

    def test_map_boundaries(self):
        in_bounds = self.map.is_in_bounds((2,2))
        too_far_west = self.map.is_in_bounds((0,10))
        too_far_east = self.map.is_in_bounds((21, 21))
        too_far_south = self.map.is_in_bounds((5,24))
        gone_home = self.map.is_in_bounds((10,0))

        assert in_bounds is True
        assert too_far_east is False
        assert too_far_west is False
        assert too_far_south is False
        assert gone_home is True

    def test_get_valid_moves(self):
        middle_of_map = self.map.get_valid_moves((5,5))
        edge_of_map = self.map.get_valid_moves((1,5))
        corner_of_map = self.map.get_valid_moves((20, 23))

        assert len(middle_of_map) == 6
        assert len(edge_of_map) == 4
        assert len(corner_of_map) == 2

