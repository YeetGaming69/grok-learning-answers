msg = input('Message? ')
step = 1
result = msg[0]
for i in range(len(msg)):
  if step <= 3:
    step += 1
  else:
    step = 2
    result += ' '
    result += msg[i]
print(result)