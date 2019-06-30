# Library used 

from bs4 import BeautifulSoup 
import pandas as pd
import requests


req = requests.get('https://distrowatch.com/dwres.php?resource=popularity')

soup = BeautifulSoup(req.text, "lxml")


i = 0
table = dict()

for sub_heading in soup.find_all('table'):
    table[i] = sub_heading
    i = i+1

i = 0
popularity = dict()
for list_pop in table[6].table.table.table.tr.find_all("table"):
    popularity[i]= list_pop
    i = i+1


popularity_dw = {}
for j in range(1,len(popularity[0].find_all("tr"))):
    
    if popularity[0].find_all("tr")[j].find_all("td")[0].get_text() in popularity_dw : 
        
        popularity_dw[popularity[0].find_all("tr")[j].find_all("td")[0].get_text()]["12_months"] = popularity[0].find_all("tr")[j].find_all("td")[1].get_text()
    else : 
        popularity_dw[popularity[0].find_all("tr")[j].find_all("td")[0].get_text()] = {}
        popularity_dw[popularity[0].find_all("tr")[j].find_all("td")[0].get_text()]["12_months"] = popularity[0].find_all("tr")[j].find_all("td")[1].get_text()
      
    if popularity[1].find_all("tr")[j].find_all("td")[0].get_text() in popularity_dw : 
        popularity_dw[popularity[1].find_all("tr")[j].find_all("td")[0].get_text()]["6_months"] = popularity[1].find_all("tr")[j].find_all("td")[1].get_text()
    else : 
        popularity_dw[popularity[1].find_all("tr")[j].find_all("td")[0].get_text()] = {}
        popularity_dw[popularity[1].find_all("tr")[j].find_all("td")[0].get_text()]["6_months"] = popularity[1].find_all("tr")[j].find_all("td")[1].get_text()
        
        
    if popularity[2].find_all("tr")[j].find_all("td")[0].get_text() in popularity_dw : 
        popularity_dw[popularity[2].find_all("tr")[j].find_all("td")[0].get_text()]["3_months"] = popularity[2].find_all("tr")[j].find_all("td")[1].get_text()
    else : 
        popularity_dw[popularity[2].find_all("tr")[j].find_all("td")[0].get_text()] = {}
        popularity_dw[popularity[2].find_all("tr")[j].find_all("td")[0].get_text()]["3_months"] = popularity[2].find_all("tr")[j].find_all("td")[1].get_text()
        
        
    if popularity[3].find_all("tr")[j].find_all("td")[0].get_text() in popularity_dw : 
        popularity_dw[popularity[3].find_all("tr")[j].find_all("td")[0].get_text()]["1_month"] = popularity[3].find_all("tr")[j].find_all("td")[1].get_text()
    else : 
        popularity_dw[popularity[3].find_all("tr")[j].find_all("td")[0].get_text()] = {}
        popularity_dw[popularity[3].find_all("tr")[j].find_all("td")[0].get_text()]["1_month"] = popularity[3].find_all("tr")[j].find_all("td")[1].get_text()


import pandas as pd 

df = pd.DataFrame.from_dict(popularity_dw, orient="index")

column = df.index

df.reset_index(level=0, inplace=True)

df.columns = ['name', '12_months',"6_months","3_months","1_month"]

df.to_csv("Distrowatch_popularity.csv")

