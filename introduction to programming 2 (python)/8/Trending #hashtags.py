import string
a = {}
b = []
c = 0
d = ''
tweet = input('Tweet: ')
while tweet != '':
  b = tweet.split()
  for word in b:
    d = word.lower()
    if d[0] == '#':
      d = d.strip(string.punctuation)
      if d in a:
        c = a[d]
        c += 1
        a[d] = c
      else:
        a[d] = 1
  tweet = input('Tweet: ')

for hashtag in a:
  print('#' + hashtag + ' ' + str(a[hashtag]))