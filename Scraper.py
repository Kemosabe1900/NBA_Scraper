import numpy as np
import time
import pandas as pd
import requests
from pprint import PrettyPrinter
import json

# show all columns in a wide DataFrame
# pd.set_option('diplay.max_columns', None)

test_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2022-23&SeasonType=Regular Season&StatCategory=PTS'
r = requests.get(url=test_url).json()
table_headers = r['resultSet']['headers']
print(pd.DataFrame(r['resultSet']['headers']))
# print(table_headers)
