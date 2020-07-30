st = input().split()

s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))
count_apples = 0
count_oranges = 0

for i in apples:
    j = i+a
    if j>=s and j<=t:
        count_apples += 1
print(count_apples)
for x in oranges:
    y = x+b
    if y>=s and y<=t:
        count_oranges +=1
print(count_oranges)