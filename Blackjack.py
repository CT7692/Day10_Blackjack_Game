############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

############### Function Definitions:

import secrets

def intro():
  clear()
  print(art.logo)
  print("Welcome to Blackjack!")

def player_hand_setup(p_hand, deck):
  for i in range(0, 2):
    player_hand.append(deck[random.randint(0, len(cards) - 1)])
  ace(p_hand)
  print("\nPlayer Hand:")
  print(f"{player_hand} = {sum(player_hand)}")

def dealer_hand_setup(d_hand, deck):
  d_hand.append('_')
  d_hand.append(deck[random.randint(0, len(deck) - 1)])
  print("\nDealer Hand:")
  print(d_hand)
  
def hit(p_hand, deck):
  p_hand.append(deck[random.randint(0, len(deck) - 1)])
  ace(p_hand)
  print(f"\nPlayer Hand: {p_hand} = {sum(p_hand)}")

def stand(p_hand):
  print(f"\nPlayer Hand:\n{p_hand} = {sum(p_hand)}")

def dealer_sequence(p_hand, d_hand, deck):
  d_hand[0] = deck[random.randint(0, len(deck) - 1)]
  if sum(d_hand) < 17 and sum(p_hand) <= 21:
    while sum(d_hand) < 17:
      d_hand.append(deck[random.randint(0, len(deck) - 1)])
      ace(d_hand)

def ace(hand):
  for i in range(0, len(hand)):
    if hand[i] == 11 and sum(hand) > 21:
      hand[i] = 1
  
def get_outcome(p_hand, d_hand):
  clear()
  if sum(p_hand) == sum(d_hand):
    print(f"\nPush!\n\nPlayer Hand: {p_hand} = {sum(p_hand)}\nDealer_Hand: {d_hand} = {sum(d_hand)}")
  elif sum(d_hand) > 21:
    print(f"\nPlayer Wins!\n\nPlayer Hand: {p_hand} = {sum(p_hand)}\nDealer_Hand: {d_hand} = {sum(d_hand)}")
  elif sum(p_hand) == 21 and sum(d_hand) != 21:
    print(f"\nPlayer Wins!\n\nPlayer Hand: {p_hand} = {sum(p_hand)}\nDealer_Hand: {d_hand} = {sum(d_hand)}")
  elif sum(p_hand) < 21 and sum(p_hand) > sum(d_hand):
    print(f"\nPlayer Wins!\n\nPlayer Hand: {p_hand} = {sum(p_hand)}\nDealer_Hand: {d_hand} = {sum(d_hand)}")
  else:
    print(f"\nDealer Wins!\n\nPlayer Hand: {p_hand} = {sum(p_hand)}\nDealer_Hand: {d_hand} = {sum(d_hand)}")

def validator(option_a, option_b, prompt):
  correct = True
  user_input = input(prompt).lower()
  if user_input != option_a and user_input != option_b:
    correct = False
    while not correct:
      print("Please type a valid option.")
      user_input = input(prompt)
      if user_input == option_a or user_input == option_b:
        correct = True
  return user_input

############### Functions Defined:

import random
import art
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
dealer_hand = []
next_move_prompt = "\nNext move? \n\nStand - Keep hand as is. \nHit - Get another card. \n\nType 'stand' or 'hit': "
keep_going_prompt = "\nKeep going? Type 'yes' or 'no': "

intro()
keep_playing = True

while keep_playing:
  player_hand_setup(player_hand, cards)
  dealer_hand_setup(dealer_hand, cards)
  next_move = validator("stand", "hit", next_move_prompt)
  if next_move == "hit":
    in_sequence = True
    while in_sequence:
      hit(player_hand, cards)
      if sum(player_hand) < 21:
        next_move = validator("stand", "hit", next_move_prompt)
      else:
        dealer_hand[0] = cards[secrets.SystemRandom().randint(0, len(cards) - 1)]
        in_sequence = False
      if next_move == "stand":
        in_sequence = False
        stand(player_hand)
        dealer_sequence(player_hand, dealer_hand, cards)
  elif next_move == "stand":
    stand(player_hand)
    dealer_sequence(player_hand, dealer_hand, cards)
  
  get_outcome(player_hand, dealer_hand)
  another_round = validator("yes", "no", keep_going_prompt)
  if another_round == "yes":
    intro()
    player_hand = []
    dealer_hand = []
  elif another_round == "no":
    keep_playing = False
    print("See ya!")
