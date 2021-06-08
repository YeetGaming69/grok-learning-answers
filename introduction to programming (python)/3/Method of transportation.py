raining = input('Is it currently raining? ')
if raining == 'Yes':
  print('You should take the bus.')
else:
  distance = int(input('How far in km do you need to travel? '))
  if distance > 10:
    print('You should take the bus.')
  elif distance <= 10 and distance >=2:
    print('You should ride your bike.')
  else:
    print('You should walk.')
  