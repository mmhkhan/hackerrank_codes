import string
import random
from random import randint
password = []
new = []
len = int(input('How long password you want (input must be greater than 5): '))
char = int(input('How many letters do you want: '))
num = int(input('How many numbers do you want: '))

for _ in range(char):
    password.append(random.choice(string.ascii_letters))
print(password)

for _ in range(num):
    password.append(str(randint(0,9)))
for _ in range(len):
    new.append(random.choice(password))

print(''.join(new))

