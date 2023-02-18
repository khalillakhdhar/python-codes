import requests
r=requests.get('http://protech-it.org/python-for-data-science/')
print(r.status_code)
print(r.headers)
print(r.content)