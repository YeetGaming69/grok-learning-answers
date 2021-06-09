a = ''
b = []
c = {}
d = 0
e = 0
with open('novel.txt') as novel:
  a = novel.read()
b = a.split()
for word in b:
  if word.istitle():
    if word in c:
      d = c[word]
      d += 1
      c[word] = d
    else:
      c[word] = 1

while e < 3:
  a = None
  d = 0
  for word in c:
    if c[word] >= d:
      a = word
      d = c[word]
  print(str(d) + ' ' + a)
  c.pop(a)
  e += 1