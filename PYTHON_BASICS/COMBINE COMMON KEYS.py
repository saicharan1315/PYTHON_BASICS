n1=int(input())
d1={}
for i in range(n1):
    k_v_pair=tuple(map(int,input().split(":")))
    d1[k_v_pair[0]]=k_v_pair[1]
print("d1 : ",d1)

n2=int(input())
d2={}
for i in range(n2):
    k_v_pair=tuple(map(int,input().split(":")))
    d2[k_v_pair[0]]=k_v_pair[1]

d3=d1.copy()

for k,v in d2.items():
    if k in d3:
        d3[k]+=v
    else:
        d3[k]=v
print(d3)
