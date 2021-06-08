time = input('Time to launch: ')
print('Counting down ...')
num = int(time)
while num > 0:
  print(str(num) + ' ...')
  num -= 1
print('Lift Off!')