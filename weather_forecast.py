import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id= 'seven-day-forecast-container')
# forecast_items = seven_day(class_ = 'tombstone-container')
# today = forecast_items[0]

# period = today.find(class_='period-name')
# desc = today.find(class_='short-desc')
# temp = today.find(class_='temp temp-high')
# img = today.find('img')
# title = img['title']
# print(period.text)
# print(desc.text)
# print(temp.text)
# print(title)

period = seven_day.select('.tombstone-container .period-name')
pts = [pt.text for pt in period]
# print(pts)

descs = seven_day.select('.tombstone-container .short-desc')
short_desc = [desc.text for desc in descs]
# print(short_desc)

temps = seven_day.select('.tombstone-container .temp')
temperature = [temp.text for temp in temps]
# print(temperature)

img_descs = [d['title'] for d in seven_day.select('.tombstone-container img')]
# print(img_descs)

weather = pd.DataFrame({
    'Short Description': short_desc,
    'Time' : pts,

'Description': img_descs,
    'Temperature': temperature

})

print(weather)