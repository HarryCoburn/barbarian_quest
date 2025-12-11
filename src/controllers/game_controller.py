class GameController:
    def __init__(self, game_map, game_state):
        self.game_map = game_map
        self.game_state = game_state

    def move_player(self, pos):
        # After validating the position, checking for getting lost, etc.
        self.game_state.current_pos = pos

    def get_valid_moves(self):
        return self.game_map.get_valid_moves(self.game_state.current_pos)