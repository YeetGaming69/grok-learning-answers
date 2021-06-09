def fix_yz(s):
  a = ''
  b = s
  for letter in b:
    if letter == 'z':
      a = a + 'y'
    elif letter == 'Z':
      a = a + 'Y'
    elif letter == 'y':
      a = a + 'z'
    elif letter == 'Y':
      a = a + 'Z'
    else:
      a = a + letter
  return(a)
      