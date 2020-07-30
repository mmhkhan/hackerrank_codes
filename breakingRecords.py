scores = list(map(int, input().rstrip().split()))
count_max = 0
count_min = 0
max_val=scores[0]
min_val=scores[0]
for i in range(1,len(scores),1):
    if scores[i]>max_val:

        max_val = scores[i]
        count_max +=1
    elif scores[i]<min_val:
        min_val = scores[i]

        count_min +=1
print(count_max, count_min)