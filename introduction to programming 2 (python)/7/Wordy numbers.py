def words2number(s):
  a = s.split()
  b = ''
  for number in a:
    if number == 'one':
      b = b + '1'
    elif number == 'two':
      b = b + '2'
    elif number == 'three':
      b = b + '3'
    elif number == 'four':
      b = b + '4'
    elif number == 'five':
      b = b + '5'
    elif number == 'six':
      b = b + '6'
    elif number == 'seven':
      b = b + '7'
    elif number == 'eight':
      b = b + '8'
    elif number == 'nine':
      b = b + '9'
    elif number == 'zero':
      b = b + '0'
  return int(b)