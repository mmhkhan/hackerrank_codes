p = list(map(int, input().rstrip().split()))
lst = [p.index(p.index(i)+1)+1 for i in range (1,len(p)+1)]
print(lst)