a = ''
b = []
a_count = 0
r_count = 0
d_count = 0
v_count = 0
k_count = 0
c = 0
with open('input.txt') as lines:
  b = lines.read()
  b = b.lower()
  b = b.splitlines()
  for line in b:
    c += 1
    a_count = line.count('a')
    r_count = line.count('r')
    d_count = line.count('d')
    v_count = line.count('v')
    k_count = line.count('k')
    if a_count >= 3:
      if r_count >= 2:
        if d_count >= 1:
          if v_count >= 1:
            if k_count >= 1:
              print('Aardvark on line ' + str(c))