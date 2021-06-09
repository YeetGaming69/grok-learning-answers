a = {}
b = input('Car: ')
c = 0
d = {}
while b != '':
  if b in a:
    c = a[b]
    c += 1
  else:
    c = 1
  d = {b : c}
  a.update(d)
  b = input('Car: ')
for colour in a:
  print('Cars that are ' + colour + ': ' + str(a[colour]))