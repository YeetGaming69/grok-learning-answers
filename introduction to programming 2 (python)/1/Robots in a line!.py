robot = input('Line: ')
robot = robot.split()
robot_num = 0
for i in robot:
  if i == 'robot':
    print('There is a small robot in the line.')
    robot_num += 1
  elif i == 'ROBOT':
    print('There is a big robot in the line.')
    robot_num += 1
  elif i.lower() == 'robot':
    print('There is a medium sized robot in the line.')
    robot_num += 1
if robot_num == 0:
  print('No robots here.')