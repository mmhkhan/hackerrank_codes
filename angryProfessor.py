nk = input().split()
n = int(nk[0])
k = int(nk[1])
a = list(map(int, input().rstrip().split()))
count=0
for i in a:
    if i<=0:
        count+=1
if count>=k: print('NO')
else: print('YES')