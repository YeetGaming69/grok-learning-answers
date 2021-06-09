order = open('orders.txt')
for line in order:
  line = line.upper()
  print(line.strip())