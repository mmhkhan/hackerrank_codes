arr = list(map(int, input().rstrip().split()))
min_sum = 0
max_sum = 0
l = len(arr)
for i in range(l-1):
    min_sum += sorted(arr)[i]
    max_sum += sorted(arr)[l-1-i]
print(min_sum, max_sum)