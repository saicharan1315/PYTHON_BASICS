s = input()
spaces = ""
result = ""
for char in s:
  if char == " ":
    spaces += char
  else:
    result += char

final = spaces + result
print(final)
