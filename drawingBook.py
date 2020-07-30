n = int(input())
p = int(input())
front_turn = p//2
if n%2==0:
    back_turn=(n-p+1)//2
elif n%2!=0:
    back_turn =(n-p)//2
if front_turn<=back_turn:
    print(front_turn)
elif front_turn>back_turn:
    print(back_turn)