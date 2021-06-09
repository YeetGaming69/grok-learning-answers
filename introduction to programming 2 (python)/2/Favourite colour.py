a = {}
b = input('Name and colour: ')
c = ''
d = ''
while b != '':
  c, d = b.split()
  a[c] = d
  b = input('Name and colour: ')
for name in a:
  print(name + ' ' + a[name])