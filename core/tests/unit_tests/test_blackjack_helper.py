from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

###################################################################

  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 7), "Drew a 7\n")
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")
    self.assertEqual(get_print(print_card_name, 14), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, -1), "BAD CARD\n")

  def test_draw_card(self):
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([5], draw_card), 5)
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([12], draw_card), 10)
    self.assertEqual(mock_random([13], draw_card), 10)

  def test_print_header(self):
    self.assertEqual(get_print(print_header, 'hello'), "-----------\nhello\n-----------\n")
    self.assertEqual(get_print(print_header, 'YO'), "-----------\nYO\n-----------\n")
    self.assertEqual(get_print(print_header, 'tEsTiNg'), "-----------\ntEsTiNg\n-----------\n")

  def test_draw_starting_hand(self):
    self.assertEqual(mock_random([4, 6], draw_starting_hand, "DEALER"), 10)
    self.assertEqual(mock_random([1, 12], draw_starting_hand, "DEALER"), 21)
    self.assertEqual(mock_random([11, 7], draw_starting_hand, "DEALER"), 17)

  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 21), "Final hand: 21.\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status, 22), "Final hand: 22.\nBUST.\n")
    self.assertEqual(get_print(print_end_turn_status, 20), "Final hand: 20.\n")

  def test_print_end_game_status(self):
    self.assertEqual(get_print(print_end_game_status, 18, 17), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 12, 22), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 18, 19), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 23, 17), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 22, 22), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 17, 17), "-----------\nGAME RESULT\n-----------\nPush.\n")
    self.assertEqual(get_print(print_end_game_status, 21, 21), "-----------\nGAME RESULT\n-----------\nPush.\n")

if __name__ == '__main__':
    unittest.main()