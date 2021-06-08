oof = input('Cars: ')
cars = oof.split()
red = 0
blue = 0
for word in cars:
  if word == 'red':
    red += 1
for word in cars:
  if word == 'blue':
    blue += 1
print('red: ' + str(red))
print('blue: ' + str(blue))
