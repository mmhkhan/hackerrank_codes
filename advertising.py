n = int(input())
cumulative = 0
shared = 5
for i in range(n):
    liked = shared//2
    cumulative += liked
    shared = liked*3
print(cumulative)