oof = input('code: ')
code = oof.split(' ')
answer = []
if oof != '':
  for i in code:
    if i[0].isupper():
      answer.append(i)
answer.reverse()
answer  = ' '.join(answer)
answer = answer.lower()
print('says: ' + answer)