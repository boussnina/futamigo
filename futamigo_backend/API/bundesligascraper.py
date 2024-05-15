from bs4 import BeautifulSoup
import cloudscraper
from time import sleep
import json

class BundesligaScraper:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()
        self.all_players = {}

    def scrape_all_teams(self):
        urls = [
            'https://www.transfermarkt.com/Borussia-Dortmund/kader/verein/16/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/fc-bayern-munchen/kader/verein/27/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/rb-leipzig/kader/verein/23826/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/bayer-04-leverkusen/kader/verein/15/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/borussia-monchengladbach/kader/verein/18/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/vfl-wolfsburg/kader/verein/82/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/fc-augsburg/kader/verein/167/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/1-fc-union-berlin/kader/verein/44/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/1-fsv-mainz-05/kader/verein/39/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/sc-freiburg/kader/verein/60/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/eintracht-frankfurt/kader/verein/24/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/vfb-stuttgart/kader/verein/79/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/tsg-1899-hoffenheim/kader/verein/533/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/sv-werder-bremen/kader/verein/86/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/sv-darmstadt-98/kader/verein/105/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/1-fc-heidenheim-1846/kader/verein/2036/saison_id/2023/plus/1',
            'https://www.transfermarkt.com/vfl-bochum/kader/verein/80/saison_id/2023/plus/1',   
            'https://www.transfermarkt.com/1-fc-koln/kader/verein/3/saison_id/2023/plus/1', 
        ]
        for url in urls:
            self._scrape_team(url)
            sleep(2)
        return json.dumps(self.all_players, indent=4)

    def scrape_team(self, url):
        self.all_players = {}  
        self._scrape_team(url)
        return json.dumps(self.all_players, indent=4, ensure_ascii=False)

    def _scrape_team(self, url):
        info = self.scraper.get(url)
        soup = BeautifulSoup(info.text, "html.parser")
        player_market_values = self._extract_market_values(soup)
        squad_name = self._extract_team_name(soup)[0]
        player_names = self._extract_player_names(soup)
        position_values = self._extract_positions(soup)
        player_data = self._extract_player_info(soup)
        player_nationalities = self._extract_nationality(soup)
        players = self._build_players_list(player_data, player_market_values, player_nationalities, player_names, position_values, squad_name)

        self.all_players[squad_name] = players

    def _extract_market_values(self, soup):
        td_elements = soup.select('td.rechts')
        return [td.a.get_text(strip=True) if td.a else 'null' for td in td_elements]

    def _extract_team_name(self, soup):
        team_name = soup.select('div[class="data-header__headline-container"]')
        return [td.get_text(strip=True) for td in team_name if td]

    def _extract_player_names(self, soup):
        player_elements = soup.select('td.hauptlink:not(.rechts)')
        return [td.a.get_text(strip=True) if td.a else 'null' for td in player_elements]

    def _extract_positions(self, soup):
        positions = soup.select('table[class="inline-table"]')
        return [p.find_all('td')[-1].get_text(strip=True) for p in positions]

    def _extract_nationality(self, soup):
        nationalities = []
        for row in soup.select('tr.odd, tr.even'):
            player_nationalities = [img['title'] for img in row.select('td.zentriert img.flaggenrahmen')]
            nationalities.append(', '.join(player_nationalities))
        return nationalities

    def _extract_player_info(self, soup):
        player_info_stats = soup.select('td.zentriert:not(.rueckennummer)')
        return [td.get_text(strip=True) for td in player_info_stats if td]

    def _build_players_list(self, player_data, market_values, nationalities, names, positions, squad_name):
        players = []
        for i in range(0, len(names)):
            player_info = player_data[i*7:i*7 + 7]
            print(player_info)
            player_dict = {
                'name': names[i] if i < len(names) else 'null',
                'position': positions[i] if i < len(positions) else 'null',
                'club': squad_name,
                'nationality': nationalities[i] if i < len(nationalities) else 'null',
                'birthdate': player_info[0] if len(player_info) > 0 else None,
                'height': player_info[2] if len(player_info) > 2 else None,
                'market_value': market_values[i] if i < len(market_values) else 'null',
                'foot': player_info[3] if len(player_info) > 3 else "null",
            }
            players.append(player_dict)
        return players

if __name__ == '__main__':
    scraper = BundesligaScraper()
    print(scraper.scrape_all_teams())



    