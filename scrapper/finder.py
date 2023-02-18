import requests
from bs4 import BeautifulSoup
# Making a GET request
r = requests.get('http://protech-it.org/python-for-data-science/')
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', class_='entry-content')
content = s.find_all('div')
print(content)