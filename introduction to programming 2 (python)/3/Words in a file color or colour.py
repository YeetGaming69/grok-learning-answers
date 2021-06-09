a = ''
b = input('Word to look for: ')
c = []
d = True
with open('book.txt') as book:
  a = book.read()
  a.lower()
  c = a.split()
  for word in c:
    if b.lower() == word.lower():
      print(b + ' was found in the book.')
      d = False
if d:
  print(b + ' was not found in the book.')