def eng2chef(s):
  a = s
  a = a.replace('tion', 'shun')
  a = a.replace('an', 'un')
  a = a.replace('th', 'z')
  a = a.replace('v', 'f')
  a = a.replace('w', 'v')
  a = a.replace('c', 'k')
  a = a.replace('o', 'oo')
  a = a.replace('i', 'ee')
  if a[-1] == '!':
    a = a.replace('!', '. bork bork bork!!')
  return a.lower()