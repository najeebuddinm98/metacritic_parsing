#parsing Metacritic ratings for Videogames using Beautiful Soup 4 library

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time

data = {"score":[], "name":[], "platform":[], "date":[]} #taking 4 pieces of information about each game

for i in range(0, 100):
    
    h = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    url = "https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?view=condensed&page={}".format(i)

    r = requests.get(url, headers = h)
    
    if r.status_code != 200:
        print(r.status_code, i)
        
    else:
        soup = BeautifulSoup(r.text, features="lxml")
        games = soup.findAll("tr", class_="expand_collapse")
        
        for game in games:
            
            score = game.find("td", class_="score").text
            data["score"].append(score.strip())
            
            name = game.find("td", class_="details").h3.text
            data["name"].append(name.strip())
            
            platform = game.find("span", class_="data").text
            data["platform"].append(platform.strip())

            date_str = game.findAll("span")[3].text.strip()
            date_dt = datetime.strptime(date_str, "%B %d, %Y") #converting the date from string to datetime object
            data["date"].append(date_dt)

    if (i%10 == 0):
        #time delay of 10 seconds after parsing of every 10 pages
        print("sleeping now for 10 seconds")
        time.sleep(10)


df = pd.DataFrame(data) 
df.to_csv("bs4_metacritic.csv")
print("Completed")
