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

    def get_valid_moves(self):
        self.game_controller.move_player((5,5)) # Force a starting position, since starting pos can be random
        valid_moves = self.game_controller.game_map.get_valid_moves(self.game_controller.game_state.current_pos)

        valid_move_set = {(5,4), (6,4), (6,5), (5,6), (4,5), (4,4)}
        assert valid_move_set.issubset(valid_moves)