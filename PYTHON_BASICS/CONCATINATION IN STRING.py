s1 = input()
s2 = input()
uncommon_chars = "".join(set(s1) ^ set(s2))
print(uncommon_chars) 
