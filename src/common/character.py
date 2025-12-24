from dataclasses import dataclass

@dataclass
class Character:
    combat_skill: int
    endurance: int
    wealth_code: int


def create_character(combat, endurance, wealth):
    return Character(combat, endurance, wealth)