cur_floor = input('Current floor: ')
des_floor = input('Destination floor: ')
floor_change = int(des_floor) - int(cur_floor)
cur_floor = int(cur_floor)
for i in range(floor_change):
  print('Level ' + str(cur_floor))
  cur_floor += 1
print('Level ' + str(des_floor))