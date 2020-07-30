n = int(input())
s = input()
counts=0
up=0
down=0
for c in s:
    if c=='D':
        down+=1
    elif c=='U':
        up+=1
    if c=='U' and up==down:
        counts+=1
print(counts)