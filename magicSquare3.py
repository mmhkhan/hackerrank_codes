from itertools import permutations
nums = list(range(1,10))
perm = list(permutations(nums,3))
rows=[]
magic=[]
for item in perm:
    if sum(item)==15:
        rows.append(item)
for k in rows:
    if k[1]%2!=0:
        if k[1]==5 or (k[0]%2==0 and k[2]%2==0):
            magic.append(k)
print(magic)
