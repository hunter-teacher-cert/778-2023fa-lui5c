# gol.py
# Luis Collado
# CSCI 77800 Fall 2023
# collaborators: none
# consulted: none

class Cell:
  def __init__(self, state):
    if state == "X" or state == True or state == 1:
      self.state = True
    else:
      self.state = False

  def __str__(self):
    return "[]" if self.state else "  "

  def set_alive(self):
    self.state = True

  def is_alive(self):
    return self.state

  


class Board:
  def __init__(self, size):
    self.size = size
    self.board = []
    for i in range(self.size):
      self.board.append([Cell(0) for i in range(self.size)])

  def __str__(self):
    returner = ""
    for row in self.board:
      for cell in row:
        returner += str(cell)
      returner += "\n"
    return returner

  def get_clean_board(self):
    newboard = []
    for i in range(self.size):
      newboard.append([Cell(0) for i in range(self.size)])
    return newboard

  def set_alive(self, x, y):
    self.board[y][x].state = True

  def count_alive_neighbors(self, x, y):
    alive_neighbors = 0
    for xmod in range(-1, 2):
      for ymod in range(-1, 2):
        newx = (x + xmod) % self.size
        newy = (y + ymod) % self.size
        if xmod == 0 and ymod == 0:
          pass
        else:
          alive_neighbors += 1 if self.board[newy][newx].is_alive() else 0
    #print(alive_neighbors)
    return alive_neighbors

  def next(self):
    # alive && 2 or 3 alive neighbors --> stay alive, else dead
    # dead && 3 alive neighbors --> come to life, else stay dead
    # make a copy of the old board
    nextboard = self.get_clean_board()
    # do checks
    for y in range(len(self.board)):
      for x in range(len(self.board[y])):
        alive_neighbors = self.count_alive_neighbors(x, y)
        #input(f'alive neighbors of {x},{y}: {alive_neighbors}')
        temp_cell = self.board[y][x]
        if not temp_cell.is_alive() and alive_neighbors == 3:
          nextboard[y][x].set_alive()
        if temp_cell.is_alive() and (alive_neighbors == 2 or alive_neighbors == 3):
          nextboard[y][x].set_alive()
    self.board = nextboard


b = Board(20)
b.set_alive(10, 9)
b.set_alive(10, 10)
b.set_alive(9, 10)
b.set_alive(9, 9)
b.set_alive(10, 8)
b.set_alive(11, 8)
b.set_alive(12, 8)
b.set_alive(11, 7)

from os import system as s
from time import sleep

print(b)

while 1 == 1:
  s('clear')
  print(b)
  sleep(0.2)
  b.next()