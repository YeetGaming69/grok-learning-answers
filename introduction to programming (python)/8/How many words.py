word = input('Word: ')
word_count = 0
words = []

while word != '':
  words.append(word)
  word = input('Word: ')
word_count = set(words) 
print('You know ' + str(len(word_count)) + ' unique word(s)!')