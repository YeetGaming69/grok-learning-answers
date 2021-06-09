import csv
word = input('Word: ')
a = {}
b = 0
c = 0

with open('scrabble_letters.txt') as scrabble:
  for row in csv.reader(scrabble, delimiter=' '): 
    a[row[1]] = row[0]

for letter in word:
  c = a[letter.upper()]
  c = int(c)
  b += c

print(str(b) + ' points')