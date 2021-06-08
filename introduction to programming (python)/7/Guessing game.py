answer = 'electricity'
print('What is my favourite food?')
guess = ''
while guess != answer:
  guess = input('Guess? ')
  if guess != answer:
    print('Not even close.')
print('You guessed it! Buzzzz')