import string
alpha = string.ascii_lowercase
h = list(map(int, input().rstrip().split()))
word = input()

dictionary = dict(zip(alpha,h))
max_value=0
for i in word:
    for keys,values in dictionary.items():
        if i==keys and max_value<values:
            max_value=values
print(max_value*len(word))