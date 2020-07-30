scores = list(map(int, input().rstrip().split()))
alice = list(map(int, input().rstrip().split()))

def binsearch(item_list,item, first, last):

    while (first<=last):
        mid = first+(last-first)//2
        if item_list[mid] == item:
            return mid
        elif item_list[mid]<item and item<item_list[mid-1]:
            return mid
        elif item_list[mid]>item and item>item_list[mid+1]:
            return mid+1
        elif item_list[mid]<item:
            last=mid-1
        elif item_list[mid]>item:
            first=mid+1
rank=[]
rank.append(1)
res=[]
for i in range(1,len(scores)):
    if scores[i]==scores[i-1]:
        rank.append(rank[i-1])
    else:
        rank.append(rank[i-1]+1)
for i in alice:
    if i<scores[len(scores)-1]:
        res.append(rank[len(scores)-1]+1)
    elif i> scores[0]:
        res.append(1)
    else:
        y = binsearch(scores, i, 0, len(scores)-1)
        res.append(rank[y])

print(res)

