n = int(input())
lst=[]
count = 0
num=n
while num!=0:
    remainder = num%10
    lst.append(remainder)
    num = num//10
for i in lst:
    if i!=0 and n%i==0:
        count+=1
print(count)