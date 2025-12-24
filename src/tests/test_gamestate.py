import unittest
from ..models.gamestate import GameState


class TestGameState(unittest.TestCase):
    def test_gamestate_creation_with_defaults(self):
        """Test that GameState can be created with default values."""
        state = GameState()
        self.assertEqual(state.current_pos, (0, 0))
        self.assertEqual(state.gold, 0)
        self.assertEqual(state.days, 1)
        self.assertEqual(state.food, 10)
        self.assertEqual(state.endurance, 9)
        self.assertEqual(state.wealth_code, 2)
        self.assertEqual(state.combat_skill, 8)
        self.assertEqual(state.wits, 6)

    def test_gamestate_creation_with_custom_values(self):
        """Test that GameState can be created with custom values."""
        state = GameState(
            current_pos=(5, 7),
            gold=100,
            days=3,
            food=5,
            endurance=12,
            wealth_code=3,
            combat_skill=10,
            wits=4
        )
        self.assertEqual(state.current_pos, (5, 7))
        self.assertEqual(state.gold, 100)
        self.assertEqual(state.days, 3)
        self.assertEqual(state.food, 5)
        self.assertEqual(state.endurance, 12)
        self.assertEqual(state.wealth_code, 3)
        self.assertEqual(state.combat_skill, 10)
        self.assertEqual(state.wits, 4)

    def test_gamestate_partial_initialization(self):
        """Test that GameState can be created with some custom values."""
        state = GameState(gold=50, days=2)
        self.assertEqual(state.gold, 50)
        self.assertEqual(state.days, 2)
        self.assertEqual(state.current_pos, (0, 0))
        self.assertEqual(state.food, 10)
        self.assertEqual(state.endurance, 9)

    def test_gamestate_attributes_are_mutable(self):
        """Test that GameState attributes can be modified."""
        state = GameState()
        state.gold = 200
        state.days = 10
        state.food = 3
        state.endurance = 5
        state.current_pos = (10, 15)

        self.assertEqual(state.gold, 200)
        self.assertEqual(state.days, 10)
        self.assertEqual(state.food, 3)
        self.assertEqual(state.endurance, 5)
        self.assertEqual(state.current_pos, (10, 15))

    def test_gamestate_equality(self):
        """Test that two GameStates with same values are equal."""
        state1 = GameState(gold=100, days=5)
        state2 = GameState(gold=100, days=5)
        self.assertEqual(state1, state2)

    def test_gamestate_inequality(self):
        """Test that two GameStates with different values are not equal."""
        state1 = GameState(gold=100, days=5)
        state2 = GameState(gold=200, days=5)
        self.assertNotEqual(state1, state2)

    def test_gamestate_position_is_tuple(self):
        """Test that current_pos is stored as a tuple."""
        state = GameState(current_pos=(3, 4))
        self.assertIsInstance(state.current_pos, tuple)
        self.assertEqual(len(state.current_pos), 2)

    def test_gamestate_with_zero_values(self):
        """Test that GameState handles zero values correctly."""
        state = GameState(gold=0, days=0, food=0, endurance=0)
        self.assertEqual(state.gold, 0)
        self.assertEqual(state.days, 0)
        self.assertEqual(state.food, 0)
        self.assertEqual(state.endurance, 0)

    def test_gamestate_with_negative_values(self):
        """Test that GameState can store negative values."""
        state = GameState(gold=-10, food=-5, endurance=-3)
        self.assertEqual(state.gold, -10)
        self.assertEqual(state.food, -5)
        self.assertEqual(state.endurance, -3)

    def test_gamestate_negative_position(self):
        """Test that GameState can handle negative position coordinates."""
        state = GameState(current_pos=(-5, -10))
        self.assertEqual(state.current_pos, (-5, -10))

    def test_gamestate_large_values(self):
        """Test that GameState can handle large values."""
        state = GameState(gold=999999, days=1000, food=500)
        self.assertEqual(state.gold, 999999)
        self.assertEqual(state.days, 1000)
        self.assertEqual(state.food, 500)
