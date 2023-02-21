#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://protech-it.org/category/formations/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

Formations=[] # a list to store quotes

table = soup.find('div', attrs = {'id':'primary'})

for row in table.findAll('article'):
	formation = {}
	formation['titre'] = row.h2.text
	formation['url'] = row.a['href']
	#formation['image']= row.img['src']
	
	Formations.append(formation)

filename = 'formations.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['titre','url'])
	w.writeheader()
	for formation in Formations:
		w.writerow(formation)