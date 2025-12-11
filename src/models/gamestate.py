from dataclasses import dataclass

@dataclass
class GameState:
    current_pos = (0,0) # This will be set to a random position from a set once we have more code
    gold = 0