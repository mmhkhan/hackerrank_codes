nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
e=100
i=0
if c[0]==1: e -= 2
while (i+k)%n!=0:

    i+=k
    if c[i%n]==0: e-=1
    elif c[i%n]==1: e-=3
    print(e)
if (i+k)%n==0: e-=1
print(e)