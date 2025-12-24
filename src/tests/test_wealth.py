import unittest
from unittest.mock import patch
from ..common.wealth import wealth_check, WEALTH_RESULT


class TestWealth(unittest.TestCase):
    def test_wealth_result_constant(self):
        """Test that WEALTH_RESULT constant is defined correctly."""
        self.assertIn(2, WEALTH_RESULT)
        self.assertEqual(WEALTH_RESULT[2], [0, 1, 2, 2, 3, 4])
        self.assertEqual(len(WEALTH_RESULT[2]), 6)

    @patch('random.randint')
    def test_wealth_check_returns_first_value(self, mock_randint):
        """Test wealth_check returns first value when roll is 1."""
        mock_randint.return_value = 1
        result = wealth_check(2)
        self.assertEqual(result, 0)
        mock_randint.assert_called_once_with(1, 6)

    @patch('random.randint')
    def test_wealth_check_returns_second_value(self, mock_randint):
        """Test wealth_check returns second value when roll is 2."""
        mock_randint.return_value = 2
        result = wealth_check(2)
        self.assertEqual(result, 1)
        mock_randint.assert_called_once_with(1, 6)

    @patch('random.randint')
    def test_wealth_check_returns_third_value(self, mock_randint):
        """Test wealth_check returns third value when roll is 3."""
        mock_randint.return_value = 3
        result = wealth_check(2)
        self.assertEqual(result, 2)
        mock_randint.assert_called_once_with(1, 6)

    @patch('random.randint')
    def test_wealth_check_returns_fourth_value(self, mock_randint):
        """Test wealth_check returns fourth value when roll is 4."""
        mock_randint.return_value = 4
        result = wealth_check(2)
        self.assertEqual(result, 2)
        mock_randint.assert_called_once_with(1, 6)

    @patch('random.randint')
    def test_wealth_check_returns_fifth_value(self, mock_randint):
        """Test wealth_check returns fifth value when roll is 5."""
        mock_randint.return_value = 5
        result = wealth_check(2)
        self.assertEqual(result, 3)
        mock_randint.assert_called_once_with(1, 6)

    @patch('random.randint')
    def test_wealth_check_returns_sixth_value(self, mock_randint):
        """Test wealth_check returns sixth value when roll is 6."""
        mock_randint.return_value = 6
        result = wealth_check(2)
        self.assertEqual(result, 4)
        mock_randint.assert_called_once_with(1, 6)

    def test_wealth_check_returns_valid_range(self):
        """Test that wealth_check returns values within expected range."""
        for _ in range(100):
            result = wealth_check(2)
            self.assertIn(result, [0, 1, 2, 3, 4])

    def test_wealth_check_with_code_2(self):
        """Test that wealth_check works with wealth code 2."""
        result = wealth_check(2)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 4)
