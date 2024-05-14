from bs4 import BeautifulSoup
import cloudscraper
from time import sleep, time
import requests
import pandas as pd





urls = [
    'https://www.transfermarkt.com/Borussia-Dortmund/kader/verein/16/saison_id/2023/plus/1',
    
        ]
scraper = cloudscraper.create_scraper()



for url in urls: 

    info = scraper.get(urls[0])
    soup = BeautifulSoup(info.text, "html.parser")
    td_elements = soup.select('td.rechts')
    
    player_market_values = []

    for td in td_elements:
        if td.a:  # Check if <a> tag exists
            value = td.a.get_text(strip=True)
        else:
            value = 'null'
        player_market_values.append(value)
player_elements = soup.select('td.hauptlink:not(.rechts)')

player_names = []
for td in player_elements:
    if td.a:  # Check if <a> tag exists
        value = td.a.get_text(strip=True)
    else:
        value = 'null'
    player_names.append(value)

players = []
player_info_stats = soup.select('td.zentriert:not(.rueckennummer)')

player_data = [td.get_text(strip=True) if td is not None else 'null' for td in player_info_stats]
# Iterate through the data in chunks of 8 (assuming each player has 8 pieces of information)
for i in range(0, len(player_data), 7):
    player_info = player_data[i:i+7]  # Get data for a single player
    player_dict = {
        'name': None,
        'position': None,
        'club': None,
        'birthdate': player_info[0] if player_info[0] else None,
        'height': player_info[2] if player_info[2] else None,
        'foot': player_info[3] if player_info[3] else 'Unknown',
        'joined': player_info[4] if player_info[4] else None,
        'signed_from': player_info[5] if player_info[5] else None,
        'contract': player_info[6] if player_info[6] else None,
        'market_value': None
    }
    players.append(player_dict)

player_market_values = soup.select('td.rechts:not(.rueckennummer)')

player_data_market_values = [td.get_text(strip=True) if td is not None else 'null' for td in player_market_values]

# Iterate through player_data and player_data_market_values simultaneously
for player_info, market_value_info in zip(players, player_data_market_values):
    # Update player_info dictionary with market_value
    player_info['market_value'] = market_value_info


for player_info, name_info in zip(players, player_names):
    player_info['name'] = name_info



df = pd.DataFrame(players)
print(df)
