from random import randint

#INTRODUCTION
intro = int(input('Welcome to Blackjack! How many players? '))
player_names = []
scores = [3] * intro
for num in range(1, intro + 1):
  names = input('What is player ' + str(num) + "'s name? ")
  player_names.append(names)

def plays():
  user_hand_values = []
  for num in range(len(player_names)):
    if scores[num] == 0:
      pass
    else:
      player = player_names[num].upper()
      user_hand = draw_starting_hand(player + "'S")
      should_hit = 'y'
      while user_hand < 21:
        should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
        if should_hit == 'n':
          break
        elif should_hit != 'y':
          print("Sorry I didn't get that.")
        else:
          user_hand = user_hand + draw_card()
      user_hand_values.append(user_hand)
      print_end_turn_status(user_hand_values[num])
  # DEALER'S TURN
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  print_end_turn_status(dealer_hand)
  # GAME RESULT
  print_end_game_status(user_hand_values, dealer_hand)
# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
  if card_rank == 1:
    card_name = 'Ace'
  elif card_rank == 11:
    card_name = 'Jack'
  elif card_rank == 12:
    card_name = 'Queen'
  elif card_rank == 13:
    card_name = 'King'
  else:
    card_name = card_rank

  if card_rank == 8 or card_rank == 1:
    print('Drew an ' + str(card_name))
  elif card_rank < 1 or card_rank > 13:
    print('BAD CARD')
  else:
    print('Drew a ' + str(card_name))

# Draws a new random card, prints its name, and returns its value.
# 
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
  card_rank = randint(1, 13)
  print_card_name(card_rank)

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    card_value = 10
  elif card_rank == 1:
    card_value = 11
  else:
    card_value = card_rank

  return card_value

# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
# 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
  print('-----------')
  print(message)
  print('-----------')

# Prints turn header and draws a starting hand, which is two cards.
# 
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
  print_header(name + ' TURN')
  return draw_card() + draw_card()

# Prints the hand total and status at the end of a player's turn.
# 
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
  print('Final hand: ' + str(hand_value) + '.')

  if hand_value == 21:
    print('BLACKJACK!')
  elif hand_value > 21:
    print('BUST.')

# Prints the end game banner and the winner based on the final hands.
# 
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand_values, dealer_hand):
  print_header('GAME RESULT')
  for num in range(len(player_names)):
    if scores[num] == 0:
      pass
    else:
      if user_hand_values[num] <= 21 and (user_hand_values[num] > dealer_hand or dealer_hand > 21):
        print(player_names[num] + ' wins! Score: ' + str(scores[num] + 1))
        scores[num] = scores[num] + 1
      elif user_hand_values[num] > 21 or (dealer_hand <= 21 and dealer_hand > user_hand_values[num]):
        print(player_names[num] + ' loses! Score: ' + str(scores[num] - 1))
        scores[num] = scores[num] - 1
      elif user_hand_values[num] == dealer_hand:
        print(player_names[num] + ' pushes. Score: ' + str(scores[num]))
        scores[num] = scores[num]
      if scores[num] == 0:
        print(player_names[num] + ' eliminated!')
      if scores == [0] * intro:
        print('All players eliminated!')
      #scores.remove(scores[num])
      #player_names.remove(player_names[num])

# Goes over the game again until the users don't want to play
# or they both get eliminted.         
def next_round():
  another_hand = input('Do you want to play another hand (y/n)? ')
  if another_hand == 'y':
    # PLAYERS TURN
    user_hand_values = []
    for num in range(len(player_names)):
      if scores[num] == 0:
        user_hand_values.insert(num, 0)
        pass
      else:
        player = player_names[num].upper()
        user_hand = draw_starting_hand(player + "'S")
        should_hit = 'y'
        while user_hand < 21:
          should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
          if should_hit == 'n':
            break
          elif should_hit != 'y':
            print("Sorry I didn't get that.")
          else:
            user_hand = user_hand + draw_card()
        user_hand_values.append(user_hand)
        print_end_turn_status(user_hand_values[num])
    # DEALER'S TURN
    dealer_hand = draw_starting_hand("DEALER")
    while dealer_hand < 17:
      print("Dealer has {}.".format(dealer_hand))
      dealer_hand = dealer_hand + draw_card()
    print_end_turn_status(dealer_hand)
    # GAME RESULT
    print_end_game_status(user_hand_values, dealer_hand)
    if scores == [0] * intro:
      return 'Game over'
    else:
      # ANOTHER ROUND
      next_round()
  elif another_hand == 'n':
    return 'Done'