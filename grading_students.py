grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
rounded = []
for i in grades:
    if i<38 or i%5<3:
        rounded.append(i)

    elif i>=38:
        rounded.append(5*round(float(i)/5))

print(rounded)
