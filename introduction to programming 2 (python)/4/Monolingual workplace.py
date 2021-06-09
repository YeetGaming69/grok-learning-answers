names = set({})
a = []
new_names = 'names'
names = input('Line: ')
a = names.split()
del a[0]
names = a

while new_names != '':
  new_names = input('Line: ')
  a = new_names.split()
  for name in a:
    if name in names:
      names.remove(name)

if names == []:
  print('Everyone is multilingual!')
else:
  for name in names:
    print(name + ' is monolingual.')
  
  
  