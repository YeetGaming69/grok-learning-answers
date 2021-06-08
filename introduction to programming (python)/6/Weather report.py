days = input('Which days had rain? ')
if days == '':
  without = 7
else:
  result = days.split(' ')
  without = 7 - len(result)
print('Number of days without rain: ' + str(without))