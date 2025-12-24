from dataclasses import dataclass

@dataclass
class GameState:
    current_pos: tuple[int,int] = (0,0) # This will be set to a random position from a set once we have more code
    gold: int = 0 # TODO There will be some starting wealth based on the wealth code
    days: int = 1
    food: int = 10
    endurance: int = 9
    wealth_code: int = 2
    wits: int = 6 # TODO Will be a random number between 2 and 6