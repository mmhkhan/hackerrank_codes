nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
count = 0
for i in range(n-1):
    for j in range(i+1,n,1):
        if (ar[i]+ar[j])%k==0:

            count+=1
print(count)