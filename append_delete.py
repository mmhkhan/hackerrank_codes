s = input()
t = input()
k = int(input())

a = list(s)
b = list(t)
if min(len(a),len(b)) ==0: x= max(len(a), len(b))
elif min(len(a),len(b))>0:
    for i in range(min(len(a),len(b))):
        if a[i]!=b[i]:
            break

    x = len(a)+len(b)-2*i
if k>=x and (k-x)%2==0 or (len(a)+len(b))<k:
    print('Yes')
else: print('No')