current = input('Current floor: ')
destination = input('Destination floor: ')
num = int(current)
while num <= int(destination):
  print('Level ' + str(num))
  num += 1