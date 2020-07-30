from collections import Counter
n = int(input())
ar = list(map(int, input().rstrip().split()))
a= Counter(ar)
pair = 0
for key, value in a.items():
    pair += value//2
print(pair)
