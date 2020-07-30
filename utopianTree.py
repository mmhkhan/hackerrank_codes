n = int(input())
height=0
for i in range(n+1):
    if i==0:
        height+=1
    elif i%2!=0:
        height*=2
    elif i%2==0:
        height +=1
print(height)