a = {}
b = input('Enter line: ')
c = 0
d = {}
e = []
f = ''
while b != '':
  e = b.split()
  for i in range(len(e)):
    f = e[i]
    if f in a:
      c = a[f]
      c += 1
    else:
      c = 1
    d = {f : c}
    a.update(d)
  b = input('Enter line: ')
for word in sorted(a):
  print(word + ' ' + str(a[word]))