import requests
from bs4 import BeautifulSoup

url = 'https://google.com'
result = requests.get(url)
print(result.text)