import csv

a = []
b = 0
c = 0
d = False
e = []
f = 0

with open('mail.txt') as class_list:
  for row in csv.reader(class_list, delimiter=','): 
    a.append(row[0])
    e.append(row[1])

name = input('Name: ')

for person in a:
  if name == person:
    d = True
    if e[f] == 'Letter':
      b += 1
    elif e[f] == 'Package':
      c += 1
  f += 1

if d == False:
  print('No mail')
else:
  if b > 0:
    if b > 1:
      print(str(b) + ' Letters')
    else:
      print(str(b) + ' Letter')
  else:
    print('No Letters')
  if c > 0:
    if c > 1:
      print(str(c) + ' Packages')
    else:
      print(str(c) + ' Package')
  else:
    print('No Packages')