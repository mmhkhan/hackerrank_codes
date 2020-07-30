arr= [-4, 3, -9, 0, 4, 1]
pos_count = 0
neg_count = 0
zero_count = 0
l = len(arr)
for i in arr:
    if i > 0:
        pos_count += 1
    elif i < 0:
        neg_count += 1
    else:
        zero_count += 1
print('%.6f' % (pos_count / l))
print('%.6f' % neg_count / l)
print('%.6f' % zero_count / l)