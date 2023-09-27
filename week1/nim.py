# nim.py
# Luis Collado
# CSCI 77800 Fall 2023
# collaborators: none
# consulted: none

print("Welcome to Nim!")

from random import randint as r

sticks_amt = 15
is_computers_turn = True

while sticks_amt > 0:
  is_computers_turn = not is_computers_turn
  print("There are", sticks_amt,"sticks in the pile.")
  print(f'{"computers" if is_computers_turn else "your"} turn!')
  if is_computers_turn:
    # choose random amt of sticks to pull
    if sticks_amt < 4:
      c = r(1, sticks_amt)
    else:
      c = r(1, 3)
    print("computer takes", c, "sticks.")
    sticks_amt -= c
  else:
    # prompt user for sticks to pull
    u = -1
    while u > 3 or u < 1 or u > sticks_amt:
      u = int(input('how many sticks would you like to pull?'))
    print("user takes", u, "sticks.")
    sticks_amt -= u

print(f'{"computer" if is_computers_turn else "user"} took the last stick!')

print(f'{"user" if is_computers_turn else "computer"} wins!')
    
  
  
    