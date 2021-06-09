a = 42
b = 0
c = 0
guess = input('Guess a multiple of 7: ')
while True:
  if c < 9:
    if guess == str(a):
      print('You won!')
      print('That was fun.')
      break
    else:
      if int(guess) % 7 == 0:
        print('Nope!')
        c += 1
      else:
        if b < 1:
          print("Mistake! That number isn't a multiple of 7.")
          b += 1
          c += 1
        else:
          print('Another mistake. Too bad.')
          print('That was fun.')
          break

    guess = input('Guess a multiple of 7: ')
  else:
    print('Nope!')
    print('No guesses left!')
    print('That was fun.')
    break