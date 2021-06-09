a = set({})
b = set({})
c = ''
d = []
with open('english.txt') as english:
  c = english.read()
  d = c.splitlines()
  for word in d:
    a.add(word)
with open('french.txt') as french:
  c = french.read()
  d = c.splitlines()
  for word in d:
    b.add(word)
for word in a:
  if word in b:
    print(word)