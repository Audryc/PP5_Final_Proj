import requests
from requests_oauthlib import OAuth1
import cnfg
from pymongo import MongoClient
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

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
zip_code.remove(11695)

#######################
##
##  Get Data from MongoDB
##
#######################

config = cnfg.load(".yelp_config")

oauth = OAuth1(config["Consumer_Key"],
               config["Consumer_Secret"],
               config["Token"],
               config["Token_Secret"])

client = MongoClient()
bus_NY_db = client.bus_NY_db
bus_NY_col = bus_NY_db.bus_NY2

#######################
##
##  Get API for each zip code
##
#######################

zip_code_pass2=[]    
for zip_cd in zip_code:
    try:
        for offset in range(0,1000,20):
            response = requests.get("https://api.yelp.com/v2/search/?location=New York, {a}&offset={b}&limit=20".format(a=zip_cd,b=offset),
                        auth=oauth)
            bus_NY_col.insert(response.json()["businesses"])
            time.sleep(1.0)
        zip_code_pass.append(zip_cd)
    except:
        pass

#######################
##
##  Create a Database
##
#######################

bus_ny_3_db = client.bus_NY_db
bus_ny3_col = bus_ny_3_db.bus_NY3
ny_bus_raw_df = pd.DataFrame(list(bus_ny3_col.find()))
ny_bus_raw_df2 = pd.DataFrame(list(bus_ny3_col.find())) #trial df

ny_bus_raw_df2 = ny_bus_raw_df2.drop_duplicates(subset='id', take_last=True)
ny_bus_raw_dfloc = ny_bus_raw_df2.location.apply(lambda x: pd.Series(x))#flatten
ny_bus_raw_df_long_lat = ny_bus_raw_dfloc.coordinate.apply(lambda x: pd.Series(x))
ny_bus_df = pd.concat([ny_bus_raw_df2[['id','name','categories','is_closed','review_count','rating']],ny_bus_raw_dfloc["postal_code"],ny_bus_raw_df_long_lat[["latitude","longitude"]]], axis=1)
ny_bus_df = ny_bus_df.dropna()
ny_bus_df["postal_code"] = ny_bus_df.postal_code.apply(lambda x: str(x))

#######################
##
##  Only use zip code from demographic data
##
#######################


pc_df = pd.DataFrame(zip_code,columns=['postal_code'])
pc_df["postal_code"] = pc_df.postal_code.apply(lambda x: str(x))
test = pd.merge(pc_df,ny_bus_df,how="inner",on=["postal_code"])


#######################
##
##  Save it to csv file
##
#######################


test.to_csv("ny_bus.csv",encoding = "utf-8")
