a = list(map(int,input().split(", ")))
b = []
m, n = map(int, input().split(", "))
for i in a:
  if i in range(m,n+1):
    b.append(i)
p = 1
for i in b:
  p *= 1
print(p)
