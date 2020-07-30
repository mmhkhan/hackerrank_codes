def div(k,a):
    for i in a:
        if k%i!=0: return False
    return True
def factor(x,b):
    for j in b:
        if j%x!=0: return False
    return True
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
all_list=[]
for i in range(min(a),min(b)+1,1):
    if factor(i,b):
        all_list.append(i)
all_set=set(all_list)
count=0
for j in all_set:
    if div(j,a):

        count+=1
print(count)