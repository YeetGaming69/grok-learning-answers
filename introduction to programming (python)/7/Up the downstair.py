number = input('How many steps? ')
print('__')
times = 1
for i in range(int(number) - 1):
  print('  ' * times + '|_')
  times += 1
print('__' * int(number) + '|')