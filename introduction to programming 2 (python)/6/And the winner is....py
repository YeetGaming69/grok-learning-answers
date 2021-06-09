import csv
a = {}
winner = ''

with open('nominees.csv') as nominees:
  for row in csv.reader(nominees, delimiter=','): 
    a[row[0]] = row[1]

win_title = input('Winning title: ')

winner = a[win_title]
print('Congratulations: ' + winner)