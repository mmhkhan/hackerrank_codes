s = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
count = 0
for j in range(len(s)-m+1):
    sum=0
    for i in range(j,j+m,1):
        sum+=s[i]
    if sum==d:
         # print(s[i])
         count+=1
print(count)