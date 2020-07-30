from bisect import bisect_left
scores = list(map(int, input().rstrip().split()))
alice = list(map(int, input().rstrip().split()))
x=list(set(scores))
sorted_scores= sorted(set(x), reverse=True)
position=[]

for i in alice:
    x.append(i)
    sorted_scores= sorted(set(x), reverse=True)
    print(sorted_scores)
    print(bisect_left(sorted_scores,i))
    # print(y)
    # position.append(y)

print(position)