import unittest
from ..common.character import Character, create_character


class TestCharacter(unittest.TestCase):
    def test_character_creation(self):
        """Test that a Character can be created with all attributes."""
        char = Character(combat_skill=8, endurance=9, wealth_code=2)
        self.assertEqual(char.combat_skill, 8)
        self.assertEqual(char.endurance, 9)
        self.assertEqual(char.wealth_code, 2)

    def test_character_dataclass_equality(self):
        """Test that two Characters with same values are equal."""
        char1 = Character(combat_skill=8, endurance=9, wealth_code=2)
        char2 = Character(combat_skill=8, endurance=9, wealth_code=2)
        self.assertEqual(char1, char2)

    def test_character_dataclass_inequality(self):
        """Test that two Characters with different values are not equal."""
        char1 = Character(combat_skill=8, endurance=9, wealth_code=2)
        char2 = Character(combat_skill=7, endurance=9, wealth_code=2)
        self.assertNotEqual(char1, char2)

    def test_create_character_function(self):
        """Test the create_character helper function."""
        char = create_character(combat=10, endurance=12, wealth=3)
        self.assertEqual(char.combat_skill, 10)
        self.assertEqual(char.endurance, 12)
        self.assertEqual(char.wealth_code, 3)

    def test_character_with_zero_values(self):
        """Test that Character can be created with zero values."""
        char = Character(combat_skill=0, endurance=0, wealth_code=0)
        self.assertEqual(char.combat_skill, 0)
        self.assertEqual(char.endurance, 0)
        self.assertEqual(char.wealth_code, 0)

    def test_character_with_negative_values(self):
        """Test that Character can be created with negative values."""
        char = Character(combat_skill=-1, endurance=-5, wealth_code=-2)
        self.assertEqual(char.combat_skill, -1)
        self.assertEqual(char.endurance, -5)
        self.assertEqual(char.wealth_code, -2)

    def test_character_attributes_are_mutable(self):
        """Test that Character attributes can be modified."""
        char = Character(combat_skill=8, endurance=9, wealth_code=2)
        char.combat_skill = 10
        char.endurance = 7
        char.wealth_code = 3
        self.assertEqual(char.combat_skill, 10)
        self.assertEqual(char.endurance, 7)
        self.assertEqual(char.wealth_code, 3)
