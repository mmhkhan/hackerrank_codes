x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])
if x1==x2 or v1==v2:
    print('NO')
else:
    y = (x1-x2)/(v2-v1)
    if y>0 and (y).is_integer(): print('YES')
    else: print('NO')
