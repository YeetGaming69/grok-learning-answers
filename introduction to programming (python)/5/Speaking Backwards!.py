msg = input('Line: ')
result = ''
for i in range(len(msg)):
  result = result + msg[-i-1]
print(result)