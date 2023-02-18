import requests
from bs4 import BeautifulSoup
# Making a GET request
r = requests.get('http://protech-it.org/python-for-data-science/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
#scraping standard all 4 above
# Getting the title tag
print(soup.title)
# Getting the name of the tag
print(soup.title.name)
# Getting the name of parent tag
print(soup.title.parent.name)
# use the child attribute to get
# the name of the child tag