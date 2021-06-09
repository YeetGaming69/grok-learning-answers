line = input('Name:vote ')
a = {}
b = {}
c = []
d = ''
e = 0

# get inputs
while line != '':
  c = line.split(':')
  if c[1] in a:
    b = a[c[1]]
    if type(b) != list:
      b = b.split()
    b.append(c[0])
    a[c[1]] = b
  else:
    a[c[1]] = c[0]
  line = input('Name:vote ')

# print outputs
for dessert in a:
  if type(a[dessert]) == list:
    for i in range(len(a[dessert])):
      if e > 0:
        d = d + ' ' + a[dessert][i]
      else:
        d = d + a[dessert][i]
      c = a[dessert]
      e += 1
  else:
    d = a[dessert]
    c = [d]
  e = 0
  
  print(dessert + ' ' + str(len(c)) + ' vote(s): ' + d)
  c = []
  d = ''