from itertools import permutations
s = []
for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))
n = [s[i][j] for i in range(3) for j in range(3)]
nums = list(range(1,10))
perm = list(permutations(nums,9))
magic=[]
for item in perm:

    if sum(item)==45 and sum(item[0:3])==15 and sum(item[3:6])==15 and sum(item[6:9])==15 and (item[0]+item[3]+item[6])==15 and (item[1]+item[4]+item[7])==15 and (item[2]+item[5]+item[8])==15 and item[4]==5:
        magic.append(list(item))

allsum = []
for l in magic:
    allsum.append(sum([abs(n[i]-l[i]) for i in range(9)]))

print(min(allsum))


