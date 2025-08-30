from RiotAPIGetMatchHistory import RiotAPIGetMatchHistory
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

#log to https://developer.riotgames.com/ and get your RIOT_API_KEY
riot_api_key = os.getenv("RIOT_API_KEY")

api = RiotAPIGetMatchHistory("Arwid", "94391", riot_api_key)
matchs = api.get_match()

columns = ["allInPings","assistMePings","assists","baronKills","champLevel","championName","commandPings","damageDealtToBuildings","deaths","detectorWardsPlaced",
             "enemyMissingPings","enemyVisionPings","getBackPings","goldEarned","goldSpent","item0","item1","item2","item3","item4","item5","item6","kills","lane","needVisionPings",
             "onMyWayPings","pushPings","role","timeCCingOthers","timePlayed","totalDamageDealtToChampions","totalMinionsKilled","totalTimeSpentDead","wardsKilled","wardsPlaced",
             "visionScore","win"]

# pd.set_option("display.max_columns", None) set this if you want print all columns
df = pd.DataFrame(matchs[0]["info"]["participants"])
df = df[columns]
print(df.head(20))

# visualize ...