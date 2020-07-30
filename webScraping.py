from bs4 import BeautifulSoup
import requests

# keyword = input('Enter a youtube keyword: ')
res = requests.get('https://www.youtube.com/results?search_query=python')
bs = BeautifulSoup(res.content,'html.parser')

elements = bs.find(id = 'contents')
print(elements.prettify())
views = elements(class_ = 'ytd-video-meta-block')
print(views)