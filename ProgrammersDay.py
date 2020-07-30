year = int(input().strip())
if year<1918:
    if year%4==0:
        s = '12.09.'+str(year)
    else:
        s = '13.09.'+str(year)
elif year==1918: s='26.09.'+str(year)
else:
    if year%400==0 or (year%4==0 and year%100!=0):
        s = '12.09.'+str(year)
    else:
        s = '13.09.'+str(year)
print(s)