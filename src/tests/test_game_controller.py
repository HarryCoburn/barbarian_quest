from ..controllers.game_controller import GameController
from ..common.map_data import map_data
from ..models.map import Map
from ..models.gamestate import GameState
import unittest

class TestGameController(unittest.TestCase):
    def setUp(self):        
        self.game_controller = GameController(Map(map_data), GameState())

    def test_move_player(self):
        self.game_controller.move_player((5,5))
        assert self.game_controller.game_state.current_pos == (5,5)