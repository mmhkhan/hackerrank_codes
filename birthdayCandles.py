ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
tall = max(ar)
count = 0
for i in ar:
    if i==tall:
        count +=1
print(count)
