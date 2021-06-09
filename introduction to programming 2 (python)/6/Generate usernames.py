import csv
first_names = []
last_names = []
a = 0
b = []
c = ''
e = 0
f = {}

with open('classlist.txt') as class_list:
  for row in csv.reader(class_list, delimiter=' '): 
    if len(row) < 3:
      first_names.append(row[0].lower())
      last_names.append(row[1].lower())
    else:
      c = row[0].lower() + row[1].lower()
      first_names.append(c)
      last_names.append(row[2].lower())
    
for name in first_names:
  if name in b:
    c = name + last_names[a][0]
    if c in b:
      if c in f:
        e = f[c]
        e += 1
        f[c] = e
      else:
        f[c] = 1
        e = 1
      c = name + last_names[a][0] + str(e)
      c.lower()
      print(c.lower())
      b.append(c)
    else:
      c.lower()
      print(c)
      b.append(c)
  else:
    c = name
    c.lower()
    print(c)
    b.append(c)
  a += 1