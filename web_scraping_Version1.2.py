

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from time import sleep
from random import randint

URL1 = 'https://meitystartuphub.in/startups/startup-wall?search=&page='
URL2 = '&domain=&location=&stage=&type='

comp = []
web = []

for page in range(1,138):
  req = requests.get(URL1 + str(page) + URL2)
  soup = bs(req.text, 'html.parser')

  containers = soup.find_all('div', class_ = 'row w-100 col-12 mx-0 align-items-center body-row mb-2')

  # sleep(randint(2,8)) # It is used to slow down the request time by random amount.

  for data in containers:
    
    name = data.find('div', class_ = 'col pl-0').text
    comp.append(name)


    
    website = data.select('a') if data.select('a') else '**No website Found **'
    try:
      website = website[0].text
    except:
      website = "No website found"
    web.append(website)

comp_list = pd.DataFrame({"Company Names " : comp , "Website Link  " : web})

comp_list.to_csv("List_of_Companies_and_Their_Website_Links_V1.2.csv")

