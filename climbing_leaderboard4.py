scores = list(map(int, input().rstrip().split()))
alice = list(map(int, input().rstrip().split()))
# x=list(set(scores))
x=scores
position=[]

for i in alice:
    x.append(i)
    sorted_scores= sorted(set(x), reverse=True)
    y = list(filter(lambda x: sorted_scores[x]==i, range(len(sorted_scores))))
    z=int("".join(map(str, y)))
    position.append(z+1)
    print(sorted_scores)
print(position)