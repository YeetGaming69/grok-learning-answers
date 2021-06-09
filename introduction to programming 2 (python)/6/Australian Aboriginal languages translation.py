a = {}
d = []
e = 0
f = ''
for words in open('dictionary.txt'):
  b, c = words.split(',')
  a[b] = c

line = input('English: ')
while line != '':
  d = line.split()
  for english in d:
    if e > 0:
      f = f + ' ' + a[english]
    else:
      f = f + a[english]
    e += 1
  f = f.replace('\n', '')
  print(f)
  f = ''
  e = 0
  line = input('English: ')