

token = "yhvGwL2FCrD0Hkgx3hIY5Qh0pBYn9AdEwmXzGw46nrhC31RNQCipdiaMKjL8"

league = "Denmark #320"

import requests
import json



url = f"https://api.sportmonks.com/v3/football/teams/countries/320?api_token={token}"

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)

data = json.loads(response.text)

print(data['data'][0])

# for item in data['data']:
#     print(item['name'] ,item['id'])
