file = input("Enter a txt file: ")

#≥
heading = "**"
subheading = "--"

# import 
from os import system, name
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

#Start
with open(file) as f:
    lines = f.readlines()
twoD = []
twoD.append([])
Sub = []
Headings = []
sub = []
con = []

def get2(a, ar, search):
  blank = []
  blank.append([])
  second = 0
  for i in (range(len(search))):
    line = search[i]
    if a in line:
      ar.append(line)
      blank.append([])
      second += 1
    blank[second].append(line)
  return blank

def get(a, ar):
  blank = []
  for i in (range(len(ar))):
    line = ar[i]
    if a in line:
      blank.append(line)
  return blank

def get3(a, ar):
  blank = []
  mode = False
  for i in (range(len(ar))):
    line = ar[i]
    if mode == True and subheading in line:
      mode = False
    if a in line:
      mode = True
    if mode:
      blank.append(line)
  return blank

twoD = get2(heading, Headings, lines)

def printhead():
  for i in (range(len(Headings))):
    line = Headings[i]
    print(str(i + 1) + ": " + line[len(subheading):])

printhead()
def getsub(ar):
  pass

def printsub(ar):
  sub = get(subheading, twoD[ar])
  for i in range(len(sub)):
    k = sub[i]
    print(str(i + 1) + ": " + k[len(subheading):])
  return sub

print()
k = input('Which Heading? ')
k = int(k)

clear()
sub = printsub(k)
def printcon(a, ar):
  content = get3(sub[a - 1], twoD[ar])
  for i in range(len(content)):
    if i == 0:
      k = content[i]
      print(k[1:])
      continue
    print(content[i])

print()
m = input('Which Sub? ')
m = int(m)
clear()
printcon(m, k)