a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
def div(k,b):

    for i in b:
        if i%k!=0: return False
    return True

factor = []
for i in a:
    for j in b:
        if j//i not in factor:
            factor.append(j//i)
count=0
for k in factor:
    if div(k,b) and k%i==0:
        count+=1
print(count)





