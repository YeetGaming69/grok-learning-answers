name = input('Enter your name: ')
if len(name) <= 3:
  print('Hi ' + name + ', you have a short name.')
elif len(name) >= 4 and len(name) <= 8:
  print('Hi ' + name + ', nice to meet you.')
else:
  print('Hi ' + name + ', you have a long name.')
  