nkq = input().split()
n = int(nkq[0])
k = int(nkq[1])
q = int(nkq[2])
a = list(map(int, input().rstrip().split()))
queries = []
for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)
temp=a
final=[]
for rot in range(k):
    new_list = []
    new_list.append(temp[len(temp)-1])
    for i in range(len(temp)-1):
        new_list.append(temp[i])
    if rot<(k-1):
        temp = new_list

for x in queries:
    final.append(new_list[x])
print(final)





