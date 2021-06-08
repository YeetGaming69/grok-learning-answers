words = input('Enter words: ')
a = words.split()
word1 = a[0]
word2 = a[1]
letter = 0
if word1[0] == word2[0]:
  if word1[-1] == word2[-1]:
    word1 = sorted(word1)
    word2 = sorted(word2)
    if word1 == word2:
      print('Super Anagram!')
    else:
      print('Huh?')
  else:
    print('Huh?')
else:
  print('Huh?')