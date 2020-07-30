from collections import Counter
arr = list(map(int, input().rstrip().split()))
a = Counter(arr)
counts = [(value,key) for key, value in a.items()]
max_count=0
max_key=0
for value,key in counts:
    if value>max_count:
        max_count= value
        max_key= key
    elif value==max_count and key<max_key:
        max_key=key
print(max_key)