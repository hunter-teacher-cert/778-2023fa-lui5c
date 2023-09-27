# exercises
# Luis Collado
# CSCI 77800 Fall 2023
# collaborators: none
# consulted: none


# Exercise 1   Draw a stack diagram for print_n called with s = 'Hello' and n=2.

'''
print_n('hello', 2)
-> print(2)
-> print_n('hello', 1)
--> print(1)
--> print_n('hello', 0)
---> return
'''

# Exercise 2   Write a function called do_n that takes a function object and a number, n, as arguments, and that calls the given function n times.

def do_n(f, n):
  for i in range(n): f()


# Exercise 3
'''
Exercise 3  
Fermat’s Last Theorem says that there are no positive integers a, b, and c such that

an + bn = cn 
for any values of n greater than 2.

Write a function named check_fermat that takes four parameters—a, b, c and n—and that checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns out to be true that
an + bn = cn 
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”

Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem.'''

def check_fermat(a, b, c, n):
  if n > 2 and a**n + b**n == c**n:
    print("Holy smokes, Fermat was wrong!")
  else:
    print("No, that doesn't work.")


def prompt():
  print("Enter four numbers, a, b, c, and n, to be checked against Fermat's theorem.")
  a = int(input("enter integer a: > "))
  b = int(input("enter integer b: > "))
  c = int(input("enter integer c: > "))
  n = int(input("enter integer n: > "))
  check_fermat(a, b, c, n)
  
  
'''
Exercise 4  
If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are one inch long, it is clear that you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test to see if it is possible to form a triangle:

If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a “degenerate” triangle.)
Write a function named is_triangle that takes three integers as arguments, and that prints either “Yes” or “No,” depending on whether you can or cannot form a triangle from sticks with the given lengths.
Write a function that prompts the user to input three stick lengths, converts them to integers, and uses is_triangle to check whether sticks with the given lengths can form a triangle.
The following exercises use TurtleWorld from Chapter 4:'''

def is_triangle(a, b, c):
  lengths = sorted([a, b, c])
  return lengths[0] + lengths[1] >= lengths[2]

def triangle_prompt():
  print("please enter 3 side lengths for a triangle.")
  a = int(input("enter side 1 length: "))
  b = int(input("enter side 2 length: "))
  c = int(input("enter side 3 length: "))
  print("thank you") if is_triangle(a, b, c) else print("that is not a triangle.")

triangle_prompt()

'''
Exercise 5  
Read the following function and see if you can figure out what it does. Then run it (see the examples in Chapter 4).'''

# I can't really figure out what it does. It looks like it would create a tree that has n many branches, and each branch is at a 50 degree angle, and each branch gets shorter until it is the last branch of length 0
# https://studio.code.org/projects/artist/AekjghpESZHykMhF5mj-wOANS2uB-7CJ0AUBtX5jlz4

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)