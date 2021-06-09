a = []
b = 0
with open('songlist.txt') as songlist:
  a = songlist.read()
  a = a.splitlines()
a.reverse()
b = input('How many more songs? ')
for song in range(int(b)):
  print(a[song])
  