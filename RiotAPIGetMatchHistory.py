import requests

class RiotAPIGetMatchHistory:
    def __init__(self, game_Name, game_id, riot_api_key,count=20,start=0):
        self.game_Name = game_Name
        self.game_id = game_id
        self.api_key = riot_api_key
        self.count = count
        self.start = start

    def get_puuid(self):
        try:
            link = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{self.game_Name}/{self.game_id}?api_key={self.api_key}"
            response = requests.get(link)
            return response.json()["puuid"]
        except Exception as e:
            print(f"error: {e}")

    def get_matchs_id(self):
        try:
            puuid = self.get_puuid()
            link = f"https://sea.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={self.start}&count={self.count}&api_key={self.api_key}"
            response = requests.get(link)
            return response.json()
        except Exception as e:
            print(f"error: {e}")

    def get_match(self):
      list_ranked_games = []
      try:
        match_id = None
        for match_id in self.get_matchs_id():
          link = f"https://sea.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.api_key}"
          response = requests.get(link)
          if response.json()["info"]['gameMode'] == "RANKED_SOLO_5x5" or "CHERRY":
            list_ranked_games.append(response.json())

      except Exception as e:
        print(f"error: {e}")

      return list_ranked_games