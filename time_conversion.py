s = input()
hr = [s[0],s[1]]
ampm = s[8]+s[9]
hours = int(hr[0])*10 + int(hr[1])
if ampm == 'AM' and hours==12:
    military_hr = '00'
elif ampm =='AM'and hours<10:
    military_hr = '0'+str(hours)
elif ampm == 'PM' and hours!=12: military_hr = hours+12
elif hours>=10: military_hr = str(hours)

mil = str(military_hr)+s[2:8]
print('{0}{1}'.format(military_hr,s[2:8]))
print(mil)

