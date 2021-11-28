import requests
from bs4 import BeautifulSoup as bs


URL1 = 'https://meitystartuphub.in/startups/startup-wall?search=&page='
URL2 = '&domain=&location=&stage=&type='

page = 1

req = requests.get(URL1 + str(page) + URL2)
soup = bs(req.text, 'html.parser')
print(soup) #Getting Whole Web Page html code as an respons