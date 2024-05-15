from bs4 import BeautifulSoup
import cloudscraper
from time import sleep
import json

class PlayerScraper:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()
        self.all_players = {}
        self.league_urls = {
            'bundesliga': [
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
            ],
            'premier_league': [
                'https://www.transfermarkt.com/arsenal-fc/kader/verein/11/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/aston-villa/kader/verein/405/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/afc-bournemouth/kader/verein/989/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/brentford-fc/kader/verein/1148/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/brighton-amp-hove-albion/kader/verein/1237/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/burnley-fc/kader/verein/1132/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/chelsea-fc/kader/verein/631/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/crystal-palace/kader/verein/873/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/everton-fc/kader/verein/29/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/fulham-fc/kader/verein/931/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/liverpool-fc/kader/verein/31/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/luton-town/kader/verein/1035/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/manchester-city/kader/verein/281/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/manchester-united/kader/verein/985/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/newcastle-united/kader/verein/762/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/nottingham-forest/kader/verein/703/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/sheffield-united/kader/verein/350/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/tottenham-hotspur/kader/verein/148/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/west-ham-united/kader/verein/379/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/wolverhampton-wanderers/kader/verein/543/saison_id/2023/plus/1'
            ],
            'la_liga': [
                'https://www.transfermarkt.com/fc-barcelona/kader/verein/131/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/real-madrid/kader/verein/418/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/atletico-madrid/kader/verein/13/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/sevilla-fc/kader/verein/368/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/real-sociedad/kader/verein/681/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/villarreal-cf/kader/verein/1050/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/athletic-bilbao/kader/verein/621/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/real-betis/kader/verein/150/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/rcd-espanyol/kader/verein/714/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/ca-osasuna/kader/verein/331/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/rc-celta-de-vigo/kader/verein/940/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/ud-almeria/kader/verein/330/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/getafe-cf/kader/verein/3709/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/real-valladolid/kader/verein/366/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/girona-fc/kader/verein/12321/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/cadiz-cf/kader/verein/2684/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/elche-cf/kader/verein/1538/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/rcd-mallorca/kader/verein/237/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/rayo-vallecano/kader/verein/367/saison_id/2023/plus/1',
                'https://www.transfermarkt.com/ud-las-palmas/kader/verein/472/saison_id/2023/plus/1'

            ]
        }

    def scrape_all_teams(self, league):
        if league not in self.league_urls:
            raise ValueError(f"League '{league}' is not supported")
        
        urls = self.league_urls[league]
        for url in urls:
            self._scrape_team(url)
            sleep(2)
        return json.dumps(self.all_players, indent=4, ensure_ascii=False)

    def scrape_team(self,league, team_name):
        if league not in self.league_urls:
            raise ValueError(f"League '{league}' is not supported")
        
        team_url = None
        for url in self.league_urls[league]:
            if team_name.lower() in url.lower():
                team_url = url
                break
        
        if not team_url:
            raise ValueError(f"Team '{team_name}' is not supported in league '{league}'")

        self._scrape_team(team_url)
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
