s = input()
t = input()
k = int(input())

a = list(s)
b = list(t)

if len(a)>len(b):
    for i in range(len(b)):
        if a[i] != b[i]:
            break
        if i==0: x = len(a)+len(b)
        elif i==len(b): x = len(a) + len(b) - 2 *i
        else: x = len(a)+len(b)-2*(i+1)
else:
    x = len(a)+len(b)

if k < x:
    print('NO')
else:
    print('YES')
    # print(x)