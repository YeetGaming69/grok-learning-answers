a = ''
b = []
with open('letter.txt') as letter:
  a = letter.read()
  b = a.splitlines()
  with open('fixed.txt', 'w') as fixed:
    for line in b:
      if 'WOOF!' in line:
        pass
      else:
        print(line, file=fixed)
