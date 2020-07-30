nk = input().rstrip().split()
k = int(nk[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
fair = (sum(bill)-bill[k])/2
if fair==b: print('Bon Appetit')
else: print(int(b-fair))