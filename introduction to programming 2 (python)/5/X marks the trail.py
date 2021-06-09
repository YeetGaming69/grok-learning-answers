size = int(input('Grid size: '))
grid = []
a = ''
location = [0 , 0]
b = 0

# make grid
for i in range(size):
  row = []
  for j in range(size):
    row.append('.')
  grid.append(row)
direction = 'a'

# print inital position
grid[0][0] = 'x'
for i in range(size):
  for j in range(size):
    a = a + grid[i][j]
  print(a)
  a = ''
while direction != '':
  direction = input('Direction: ')
  if direction == 'right':
    location[0] += 1
  elif direction == 'left':
    location[0] -= 1
  elif direction == 'up':
    location[1] -= 1
  elif direction == 'down':
    location[1] += 1
  else:
    b += 1
  if b < 1:
    grid[location[1]][location[0]] = 'x'
    for i in range(size):
      for j in range(size):
        a = a + grid[i][j]
      print(a)
      a = ''
  
  