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
        

