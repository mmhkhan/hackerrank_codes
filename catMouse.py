xyz = input().split()
x = int(xyz[0])
y = int(xyz[1])
z = int(xyz[2])
if abs(x-z)>abs(y-z):
    print('Cat B')
elif abs(x-z)<abs(y-z):
    print('Cat A')
else: print('Mouse C')