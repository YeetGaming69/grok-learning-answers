a = set({})
b = input('Guess: ')
while b != '':
  if b in a:
    print("You've chosen that square already")
  else:
    print('Hit ' + b)
    a.add(b)
  b = input('Guess: ')