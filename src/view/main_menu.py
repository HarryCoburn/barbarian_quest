import dearpygui.dearpygui as dpg
import random
from ..models.gamestate import GameState
from ..common.game_text import GameText, TextCategory
from .view import View


STARTING_HEXES = [(1, 1), (7, 1), (8, 1), (13, 1), (15, 1), (18, 1)]


def select_starting_hex() -> tuple[int, int]:
    """
    Randomly select a starting hex from the valid starting positions.

    Returns:
        A tuple (x, y) representing the starting hex coordinates
    """
    return random.choice(STARTING_HEXES)


class MainMenu:
    def __init__(self):
        self.game_view = None

        with dpg.window(label="Barbarian Quest - Main Menu", tag="main_menu_window") as self.menu_window:
            dpg.add_text("Barbarian Quest", tag="title_text")
            dpg.add_spacer(height=20)
            dpg.add_text("A quest to reclaim your kingdom")
            dpg.add_spacer(height=40)

            self.start_button = dpg.add_button(
                label="Start Game",
                callback=self.start_game,
                width=200,
                height=50
            )

    def start_game(self):
        """Initialize and start a new game"""
        # Select random starting hex
        starting_hex = select_starting_hex()

        # Create game state with starting position
        game_state = GameState(
            current_pos=starting_hex,
            gold=0,
            days=1,
            food=10,
            endurance=9
        )

        # Hide main menu
        dpg.hide_item(self.menu_window)

        # Create game view
        self.game_view = View(game_state)

        # Show intro text
        intro_text = GameText.get_text(TextCategory.INTRO, "opening")
        self.game_view.update_info(intro_text)

        # Set the game window as primary
        dpg.set_primary_window("main_window", True)
