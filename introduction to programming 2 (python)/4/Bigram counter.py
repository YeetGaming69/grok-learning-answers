a = {}
line = input('Line: ')
b = []
c = ''
d = 0
while line != '':
  line = line.lower()
  b = line.split()
  d = len(b) - 1
  for i in range(d):
    c = b[i] + ' ' + b[i + 1]
    if c in a:
      a[c] += 1
    else:
      a[c] = 1
  line = input('Line: ')
for word in a:
  if a[word] > 1:
    print(word + ': ' + str(a[word]))