import unittest
import main
from function_guess import guess_number


class TestCase:
    pass


class TestGuessNumber(unittest.TestCase):

    def test_correct_guess(self):
        # Test the case where the guess is correct
        result = guess_number(5, 5)
        self.assertEqual(result, "Whoa you are a genius!")

    def test_incorrect_guess(self):
        # Test the case where the guess is incorrect
        result = guess_number(3, 5)
        self.assertIsNone(result)

    def test_non_integer_input(self):
        # Test the case where the input is not an integer
        with self.assertRaises(ValueError):
            guess_number("a", 5)

    def test_negative_number(self):
        # Test the case where the input is a negative number
        result = guess_number(-1, 5)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
