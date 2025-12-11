from dataclasses import dataclass

@dataclass
class GameState:
    current_pos: tuple[int,int] = (0,0) # This will be set to a random position from a set once we have more code
    gold: int = 0