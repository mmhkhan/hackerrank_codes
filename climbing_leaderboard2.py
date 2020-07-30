scores = list(map(int, input().rstrip().split()))
alice = list(map(int, input().rstrip().split()))
# x=list(set(scores))
x=scores
position=[]

for i in alice:
    x.append(i)
    sorted_scores= sorted(set(x), reverse=True)
    y = sorted_scores.index(i)
    position.append(y+1)
print(position)