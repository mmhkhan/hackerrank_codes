a = list(map(int, input().rstrip().split()))
print(max([sum((a.count(i), a.count(i+1))) for i in set(a)]))