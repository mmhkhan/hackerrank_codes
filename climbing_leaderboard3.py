scores = list(map(int, input().rstrip().split()))
alice = list(map(int, input().rstrip().split()))
# x=list(set(scores))
x=scores
position=[]

for i in alice:
    x.append(i)
    sorted_scores= sorted(set(x), reverse=True)
    for j,k in enumerate(sorted_scores):
        if k==i:

            y = j+1
    position.append(y+1)
    print(sorted_scores)
print(position)