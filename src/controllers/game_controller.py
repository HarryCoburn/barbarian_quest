class GameController:
    def __init__(self, game_map, game_state):
        self.map = game_map
        self.game_state = game_state

    def move_player(self, pos):
        # After validating the position, checking for getting lost, etc.
        self.game_state.current_pos = pos