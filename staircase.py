n = int(input())
k=1
for j in range(n,0,-1):
    for i in range(1,n+1):
        if i<j: print(' ',end='')
        if i==j: print(k*'#', end='')
    k +=1
    print()
