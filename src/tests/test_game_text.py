import unittest
from ..common.game_text import GameText, TextCategory


class TestGameText(unittest.TestCase):
    def test_get_intro_text(self):
        intro = GameText.get_text(TextCategory.INTRO, "opening")
        self.assertIsNotNone(intro)
        self.assertIn("Evil events", intro)
        self.assertIn("500 gold pieces", intro)
        self.assertIn("ten weeks", intro)

    def test_get_nonexistent_text_returns_none(self):
        result = GameText.get_text(TextCategory.INTRO, "nonexistent_key")
        self.assertIsNone(result)

    def test_get_all_texts_in_category(self):
        intro_texts = GameText.get_category(TextCategory.INTRO)
        self.assertIsInstance(intro_texts, dict)
        self.assertIn("opening", intro_texts)

    def test_text_category_enum_has_required_categories(self):
        self.assertTrue(hasattr(TextCategory, "INTRO"))
        self.assertTrue(hasattr(TextCategory, "EVENT"))
        self.assertTrue(hasattr(TextCategory, "LOCATION"))
        self.assertTrue(hasattr(TextCategory, "ENCOUNTER"))

    def test_format_text_with_variables(self):
        formatted = GameText.format_text(TextCategory.EVENT, "new_day", day=5)
        self.assertEqual(formatted, "A new day begins. Day 5.")

    def test_format_text_nonexistent_returns_none(self):
        result = GameText.format_text(TextCategory.EVENT, "nonexistent", day=1)
        self.assertIsNone(result)
