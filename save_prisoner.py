nms = input().split()
n = int(nms[0])
m = int(nms[1])
s = int(nms[2])
iter = s+m-1
if iter%n!=0:
    warn = iter%n
else:
    warn = n

print(warn)