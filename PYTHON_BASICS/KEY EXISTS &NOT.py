import operator
d={}
n = int(input("no of elements:"))
for i in range(n):
  k = input("enter key for dict:")
  v = input("enter its value:")
  d[k]=v
key=input()
if key in d:
  print('Key is present in the dictionary')
else:
  print('Key is not present in the dictionary')