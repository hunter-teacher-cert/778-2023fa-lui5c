"""This program simulates the sales of tickets for a specific flight.

A plane is represented by a list. Each element of the list is a row in
the plane (with plane[0] being the front) and reach row is also a
list.

Seats can be purchased as economy_plus or regular economy.

Economy_plus passengers select their seats when they purchase their tickts.
Economy passengers are assigned randomly when the flight is closer to full

"""
import random

"""
Creates and returns a plane of size rowsxcols
Plans have windows but no aisles (to keep the simulation simple)
S is seat
W is window
X is taken
"""
def create_plane(rows,cols):
  return [['W' if (col == 0 or col == cols-1) else 'S' for col in range(cols)] for row in range(rows)]
  

"""   
Input: a dicitonary containing the 
number of regular economy seats sold. 
the keys are the names for the tickets
and the values are how many

ex: {'Robinson':3, 'Lee':2 } // The Robinson 
family reserved 3 seats, the Lee family 2

Returns: the total number of seats sold"""
def get_number_economy_sold(economy_sold):
  return sum(economy_sold.values())

"""  
Parameters: plane : a list of lists representing plane
economy_sold : a dictionary of the economy seats sold but
               not necessarily assigned

Returns: the number of unsold seats

Notes: this loops over the plane and counts the number of seats
       that are "avail" or "win" and removes the number of
       economy_sold seats"""

def get_avail_seats(plane,economy_sold):
  #already_sold_economy = get_number_economy_sold(economy_sold)
  taken_seats = sum([1 if seat not in ["W", "S"] else 0 for seat in sum(plane, [])])
  return get_total_seats(plane) - taken_seats - sum(economy_sold.values())


"""  
Params: plane : a list of lists representing a plane
Returns: The total number of seats in the plane
"""
def get_total_seats(plane):
  return sum([1 for seat in sum(plane, [])])



"""  
Params: plane : a list of lists representing a plane
Returns: a string suitable for printing. """
def get_plane_string(plane):
  string = ""
  for row in plane: 
    string += "\t\t".join(row) + " \n"
  return string


"""  
Params: plane - a list of lists representing a plane

economy_sold - a dictionary representing the economy
               sold but not assigned
name - the name of the person purchasing the seat

This routine randomly selects a seat for a person purchasing
economy_plus. Preference is given to window and front seats."""
def purchase_economy_plus(plane,economy_sold,name):
  row = 0
  seat_found = False
  while not seat_found:
    choice = random.choices(
      [i for i in range(len(plane[0]))], # population
      weights = [1 if (i == 0 or i == len(plane[0])-1) else 0.05 
                 for i in range(len(plane[0]))]
    )[0]
    #print(choice)
    if plane[row][choice] not in ["W", "S"]: 
      row = row + 1 if row < len(plane)-1 else 0
    else:
      plane[row][choice] = name
      seat_found = True
  return plane
    
"""  
Similar to purchase_economy_plus but just randomy assigns
a random seat.
"""
def seat_economy(plane,economy_sold,name):
  flatplane = [seat if seat in ["W", "S"] else 0 for seat in sum(plane,[])]
  options = [i if flatplane[i] != 0 else 0 for i in range(len(flatplane))]
  #print(flatplane)
  choice = random.choice(options)
  while choice == 0: choice = random.choice(options)
  index = options.index(choice)
  c = index % len(plane[0])
  r = (index - c) // len(plane[0])
  #print(index, '-->', r, c)
  #print(get_plane_string(plane))
  #input()
  if plane[r][c] in ["W", "S"]:
    plane[r][c] = name
  return plane
  print(get_plane_string(plane))

def seat_economy_family(plane, economy_sold, name):
  #print(economy_sold[name])
  familysize = economy_sold[name]
  rowsize = len(plane[0])
  rows = len(plane)
  # row - size options
  for r in range(rows-1, 0, -1):
    row = plane[r]
    for i in range(rowsize - familysize + 1):
      if set(row[i:i+familysize]).issubset(set(('S', "W"))):
        for j in range(familysize):
          row[i+j] = name
        return plane
  for i in range(economy_sold[name]):
    seat_economy(plane, economy_sold, name)
  return plane
  
"""  
Purchase regular economy seats. As long as there are sufficient seats
available, store the name and number of seats purchased in the
economy_sold dictionary and return the new dictionary
"""
def purchase_economy_block(plane,economy_sold,number,name):
  avail = get_avail_seats(plane, economy_sold)
  if avail >= number:
    economy_sold[name] = number
  return economy_sold

"""
takes an empty plane and runs our simulation to sell seats and then
seat the economy passengers. See comments in the function for details. 
"""
def fill_plane(plane):
  economy_sold = {}
  # first, economy plus choose
  economy_plus_count = 0
  while get_avail_seats(plane, economy_sold) > 0.7*get_total_seats(plane):
    plane = purchase_economy_plus(plane, economy_sold, f'p{economy_plus_count}')
    economy_plus_count += 1
    
  # then, economy are assigned
  economy_count = 0
  while get_avail_seats(plane, economy_sold) > 0:
    amt = random.randint(1,3)
    economy_sold = purchase_economy_block(plane, economy_sold, amt,f'e{economy_count}')
    economy_count += 1
    #print(get_avail_seats(plane, economy_sold))
    #input()
  individuals = []
  for name in economy_sold:
    #print(get_plane_string(plane))
    #input()
    if (economy_sold[name] == 1):
      individuals.append(name)
    else: 
      plane = seat_economy_family(plane, economy_sold, name)
  for name in individuals:
    plane = seat_economy_family(plane, economy_sold, name)
  return plane

    
def main():
  plane = create_plane(10,5)
  plane = fill_plane(plane)
  print(get_plane_string(plane))
if __name__=="__main__":
    main()