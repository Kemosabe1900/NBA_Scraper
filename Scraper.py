import pandas as pd
import requests
# show all columns in a wide DataFrame
pd.set_option('diplay.max_colums', None)

test_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2022-23&SeasonType=Regular%20Season&StatCategory=PTS"
# r = requests.get(url =  ).json
