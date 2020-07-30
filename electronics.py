bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
max_spent=0
for i in keyboards:
    for j in drives:
        pair=i+j
        if max_spent<pair and pair<=b:
            max_spent = pair
if max_spent>0:
    print(max_spent)
elif max_spent==0:
    print(-1)
