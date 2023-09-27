# card_matches.py
# Luis Collado
# CSCI 77800 Fall 2023
# collaborators: none
# consulted: none

import random


class Playing_Card:
  suits = {
    "clubs": "♣",
    "diamonds": "♦", 
    "hearts": "♥",
    "spades": "♠"
  }
  values = {
    "A": 14,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
  }
  
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit

  def print_val(self):
    print(f"This card is the {self.value} of {self.suit}s.")

  def compare(self, other):
    if Playing_Card.values[self.value] > Playing_Card.values[other.value]:
      return ">"
    elif Playing_Card.values[self.value] < Playing_Card.values[other.value]:
      return "<"
    else:
      return "=="

  def set_value(self, value):
    self.value = value

  def get_value(self):
    return self.value

  def set_suit(self, suit):
    self.suit = suit

  def get_suit(self):
    return self.suit

  def __str__(self):
    return f"{Playing_Card.suits[self.suit]}{self.value}"

  def __add__(self, other):
    return Playing_Card.values[self.value] + Playing_Card.values[other.value]

  def __lt__(self, other):
    return Playing_Card.values[self.value] < Playing_Card.values[other.value]

  def __gt__(self, other):
    return Playing_Card.values[self.value] > Playing_Card.values[other.value]

  def __eq__(self, other):
    return Playing_Card.values[self.value] == Playing_Card.values[other.value]

  def __repr__(self):
    return str(self)


class Hand_Of_Cards:
  def __init__(self):
    self.cards = []

  def addCard(self, card):
    self.cards.append(card)

  def removeRandom(self):
    toRemove = random.choices(self.cards)
    self.cards.remove(toRemove)
    return toRemove

  def hasMatch(self, other):
    return len(set(
      [Playing_Card.values[c.value] for c in self.cards])
               .intersection(
      [Playing_Card.values[c.value] for c in other.cards]))

  def __str__(self):
    return " ".join([str(card) for card in self.cards])


master_deck = []

for suit in ["hearts", "clubs", "diamonds", "spades"]:
  for value in [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]:
    master_deck.append(Playing_Card(value, suit))

# comparison test
master_deck.sort()

print("sorted deck:")

# string output test
print(master_deck)

print("shuffled deck:")
random.shuffle(master_deck)
print(master_deck)

h1 = Hand_Of_Cards()
h2 = Hand_Of_Cards()

for i in range(5): h1.addCard(master_deck.pop(random.randint(0, len(master_deck)-1)))
for i in range(5): h2.addCard(master_deck.pop(random.randint(0, len(master_deck)-1)))

print("hand 1: ", h1)
print("hand 2: ", h2)
print("amount of matches: ", h1.hasMatch(h2))