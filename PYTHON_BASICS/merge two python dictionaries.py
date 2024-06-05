d = {}
d1 = {}
n = int(input("no of elements:"))
for i in range(n):
  k = input("enter key for dict:")
  v = input("enter its value:")
  d[k]=v

for i in range(n):
  k = input("enter key for dict:")
  v = input("enter its value:")
  d1[k]=v
d2 = d.copy()
d2.update(d1)
print(d2)
