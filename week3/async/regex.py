# regex.py
# Luis Collado
# CSCI 77800 Fall 2023
# collaborators: none
# consulted: regexr

import re

def find_date(line):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    result = re.findall(pattern,line)

    pattern=r'(October|Oct|November|Nov)( [0-9]{1,2}, [0-9]{4})'
    result = result + re.findall(pattern,line)
    return result

def find_name(line):
  pattern = r"(((((([A-Z])\w+)+[\.])+)|(([A-Z])\w+))( )([A-Z]\w+)\w+)"
  result = re.findall(pattern, line)
  return [t[0] for t in result]


f = open("week3_async/datefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)