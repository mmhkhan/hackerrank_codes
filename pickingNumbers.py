from collections import Counter
a = list(map(int, input().rstrip().split()))
count = Counter(a)
# sort_count = sorted(count)
setA=list(set(a))
print(count)
print(setA)
keys=[]
# j=0
for i in range(len(setA)-1):
    if abs(setA[i]-setA[i+1])==1:
        keys.append(setA[i])
for j in range(len(keys)-1):
    if keys[j+1]-keys[j]==1:
        sub = [keys[k:k+2] for k in range(2)]
print(sub)
print(keys)
sum=0
for i in keys:
    for key, value in count.items():
        if i==key:
            sum+=value
print(sum)



