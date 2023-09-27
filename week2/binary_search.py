# binary_search.py
# Luis Collado
# CSCI 77800 Fall 2023
# collaborators: none
# consulted: none


from random import randint as r

array = [r(0, 10) for i in range(10)]

array = sorted(array)

print(array)

def bin_search(haystack, needle):
  lo_idx = 0
  hi_idx = len(haystack) - 1
  while hi_idx != lo_idx:
    m_idx = (hi_idx + lo_idx) // 2
    if haystack[m_idx] > needle:
      hi_idx = m_idx
    elif haystack[m_idx] < needle:
      lo_idx = m_idx + 1
    else:
      return m_idx
  return lo_idx if haystack[lo_idx] == needle else -1

for i in range(len(array)):
  print(f'bin search for {array[i]} returns \t{bin_search(array, array[i])}')