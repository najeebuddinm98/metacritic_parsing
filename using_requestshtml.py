#parsing Metacritic ratings for Videogames using Requests-HTML library

from requests_html import HTMLSession
from datetime import datetime
import pandas as pd
import time

data = {"score":[], "name":[], "platform":[], "date":[]}

for i in range(0, 100):
    
    url = "https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?view=condensed&page={}".format(i)
    session = HTMLSession()
    
    r = session.get(url)
    
    if r.status_code != 200:
        print(r.status_code, i)

    else:
        
        h = r.html
        games = h.find("tr.expand_collapse")
        
        for game in games:
            
            score = game.find("td.score", first=True).text
            data["score"].append(score.strip())
            
            name = game.find("h3")[0].text
            data["name"].append(name.strip())
            
            platform = game.find("span.data")[0].text
            data["platform"].append(platform.strip())

            date_str = game.find("span")[3].text.strip()
            date_dt = datetime.strptime(date_str, "%B %d, %Y") #converting the date from string to datetime object
            data["date"].append(date_dt)

    if (i%10 == 0):
        #time delay of 10 seconds after parsing of every 10 pages
        print("sleeping now for 10 seconds")
        time.sleep(10)


df = pd.DataFrame(data)
df.to_csv( "requestshtml_metacritic.csv" )
print("Completed")
