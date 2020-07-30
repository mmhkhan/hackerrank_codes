ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])
nums = [x for x in range(i,j+1)]
count = 0
for y in nums:
    reverse = 0
    y_new=y
    while(y_new>0):
        remainder = y_new%10
        reverse=reverse*10 + remainder
        y_new= y_new//10
    if abs(reverse-y)%k ==0:
        count += 1
print(count)


