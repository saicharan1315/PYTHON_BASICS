def swap(str1):
  res = ""
  for i in str1:
    if i.isupper():
      res += i.lower()
    else:
      res += i.upper()
  return res
str1 = input()
print(swap(str1))
