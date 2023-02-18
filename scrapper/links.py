import requests
from bs4 import BeautifulSoup
# Making a GET request
r = requests.get('http://protech-it.org/python-for-data-science/')
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
# find all the anchor tags with "href"
for link in soup.find_all('a'):
    print(link.get('href'))