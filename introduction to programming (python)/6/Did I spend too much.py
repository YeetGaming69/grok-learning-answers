numbers = input('Enter the expenses: ')
seperated = numbers.split(' ')
answer = 0
if seperated == ['']:
  pass
else:
  for i in range(len(seperated)):
    answer += int(seperated[i])
print('Total: $' + str(answer))