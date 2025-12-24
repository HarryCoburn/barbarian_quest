import unittest
import dearpygui.dearpygui as dpg
from ..view.main_menu import MainMenu
from ..models.gamestate import GameState


class TestMainMenu(unittest.TestCase):
    def setUp(self):
        dpg.create_context()
        self.main_menu = MainMenu()

    def tearDown(self):
        dpg.destroy_context()

    def test_main_menu_has_start_button(self):
        self.assertTrue(dpg.does_item_exist(self.main_menu.start_button))

    def test_start_button_has_correct_label(self):
        label = dpg.get_item_label(self.main_menu.start_button)
        self.assertEqual(label, "Start Game")

    def test_main_menu_window_exists(self):
        self.assertTrue(dpg.does_item_exist(self.main_menu.menu_window))


class TestStartingHexSelection(unittest.TestCase):
    def test_starting_hex_is_valid(self):
        valid_starting_hexes = [(1, 1), (7, 1), (8, 1), (13, 1), (15, 1), (18, 1)]
        game_state = GameState()

        # Test multiple times to ensure randomness works
        for _ in range(10):
            from ..view.main_menu import select_starting_hex
            starting_hex = select_starting_hex()
            self.assertIn(starting_hex, valid_starting_hexes)

    def test_starting_hex_selection_is_random(self):
        from ..view.main_menu import select_starting_hex

        # Collect multiple selections
        selections = set()
        for _ in range(50):
            selections.add(select_starting_hex())

        # With 50 iterations, we should get more than one unique result
        # (probability of getting only one is astronomically low)
        self.assertGreater(len(selections), 1)
