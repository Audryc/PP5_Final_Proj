import requests
from requests_oauthlib import OAuth1

from bs4 import BeautifulSoup
import requests

#######################
##
##  Get Zip Code
##
#######################


url0 = "https://www.health.ny.gov/statistics/cancer/registry/appendix/neighborhoods.htm"
response = requests.get(url0)
page = response.text
soup = BeautifulSoup(page)
zip_code_ls = []
for zip_code in soup.findAll(headers="header3"):
    zip_code_ls = zip_code_ls + str(zip_code.getText()).split(',')
zip_code = map(int,zip_code_ls)

#######################
##
##  Scrap Demo Data
##
#######################


demo_dict = {}
for val in zip_code:
    url1 = "http://www.city-data.com/zips/{zi}.html".format(zi = val)
    response = requests.get(url1)
    page = response.text
    soup = BeautifulSoup(page)

    demo_dict[val] = soup

del demo_dict[11695]
print len(demo_dict)

#######################
##
##  Create Data
##
#######################

from parse import *
pop_dict = []
for key in demo_dict:
    a = {}
    try:
        a['postal_code']=key
        a['population']=int(filter(lambda x: x.isdigit(), search('zip code population in 2013:</b> {}<br/>', str(demo_dict[key].findAll(class_='row')))[0]))
        income = [x for x in search('Estimated median household income in 2013: </b></b><table><tr><td><b>This zip code:{}<b>', str(demo_dict[key].findAll()))[0].split('>') if '$' in x]
        a['median_income'] = int(filter(lambda x: x.isdigit(), income[0]))
        hsh = [x for x in search('Average household size:</b><table><tr><td><b>This zip code:{}<b>', str(demo_dict[key].findAll()))[0].split('>') if 'people' in x]
        a['household_size'] = float(hsh[0].split()[0])
    except:
        if key == 11359:
            a['postal_code']=key
            a['population']=5963
            a['median_income'] = 73237
            hsh = [x for x in search('Average household size:</b><table><tr><td><b>This zip code:{}<b>', str(demo_dict[key].findAll()))[0].split('>') if 'people' in x]
            a['household_size'] = float(hsh[0].split()[0])
        elif key == 10020:
            a['postal_code']=key
            a['population']=70
            a['median_income'] = 91974
            hsh = [x for x in search('Average household size:</b><table><tr><td><b>This zip code:{}<b>', str(demo_dict[key].findAll()))[0].split('>') if 'people' in x]
            a['household_size'] = float(hsh[0].split()[0])
    pop_dict.append(a)

#######################
##
##  Create data frame and save it to csv
##
#######################

import pandas as pd
pop_df = pd.DataFrame(pop_dict)

pop_df.to_csv("pop_zip.csv")
pop_df.head()


