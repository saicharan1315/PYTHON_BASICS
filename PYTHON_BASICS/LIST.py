n1 = ['python', 'flask', 'django', 'tkinter']
n2 = n1
n3 = n1[:2]
n2[0] = 'scipy'
n3[1] = 'Numpy'
s = 10
for i in (n1, n2, n3):
  if i[0] == 'python':
    s += 1
  if i[1] == 'python':
    s += 2
print(s)
