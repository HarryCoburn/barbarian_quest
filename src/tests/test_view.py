from ..view.view import View, HexGrid
from ..models.gamestate import GameState
import unittest
import dearpygui.dearpygui as dpg

class TextHexGrid(unittest.TestCase):
    def setUp(self):
        self.grid = HexGrid(radius=30, spacing=60)

    def test_game_to_screen_conversion(self):
        screen_x, screen_y = self.grid.game_to_screen((5,5))

class TestView(unittest.TestCase):
    def setUp(self):
        dpg.create_context()
        self.game_state = GameState(current_pos=(5, 5), gold=100, days=3, food=8, endurance=15)
        self.view = View(self.game_state)

    def tearDown(self):
        dpg.destroy_context()

    def test_view_has_stats_area(self):
        self.assertTrue(dpg.does_item_exist(self.view.stats_container))

    def test_view_displays_days(self):
        self.assertTrue(dpg.does_item_exist(self.view.days_text))
        self.assertEqual(dpg.get_value(self.view.days_text), "Days: 3")

    def test_view_displays_food(self):
        self.assertTrue(dpg.does_item_exist(self.view.food_text))
        self.assertEqual(dpg.get_value(self.view.food_text), "Food: 8")

    def test_view_displays_gold(self):
        self.assertTrue(dpg.does_item_exist(self.view.gold_text))
        self.assertEqual(dpg.get_value(self.view.gold_text), "Gold: 100")

    def test_view_displays_endurance(self):
        self.assertTrue(dpg.does_item_exist(self.view.endurance_text))
        self.assertEqual(dpg.get_value(self.view.endurance_text), "Endurance: 15")

    def test_view_has_info_area(self):
        self.assertTrue(dpg.does_item_exist(self.view.info_text))

    def test_view_has_button_area(self):
        self.assertTrue(dpg.does_item_exist(self.view.button_container))

    def test_view_has_map_area(self):
        self.assertTrue(dpg.does_item_exist(self.view.map_canvas))

    def test_update_stats_changes_display(self):
        self.game_state.days = 5
        self.game_state.gold = 200
        self.view.update_stats(self.game_state)
        self.assertEqual(dpg.get_value(self.view.days_text), "Days: 5")
        self.assertEqual(dpg.get_value(self.view.gold_text), "Gold: 200")

    def test_update_info_text(self):
        self.view.update_info("You encounter a merchant.")
        self.assertIn("You encounter a merchant.", dpg.get_value(self.view.info_text))

    def test_info_text_widget_has_wrap_enabled(self):
        wrap_value = dpg.get_item_configuration(self.view.info_text)['wrap']
        self.assertEqual(wrap_value, 560)


