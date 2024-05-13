from flask import Flask, jsonify
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/statistics')
def statistics():
    data = [
        {
            'home_team': 'Real Madrid',
            'visitor_team': 'Manchester City',
            'result': '1-0'
        },
        {
            'home_team': 'Real Sociedad',
            'visitor_team': 'Manchester United',
            'result': '3-0'
        }
    ]
    return jsonify(data)

@app.route('/futl/<string:player_name>')
def futl(player_name):
    players = []
    data = [
        {
            'name': 'Ronaldinho',
            'club': 'Barcelona',  # Corrected the spelling of Barcelona
            'nationality': 'Brazilian',
            'age': '48',
            'position': 'Midfield',
            'strong foot': 'Right'
        },
        {
            'name': 'Lionel Messi',
            'club': 'Paris Saint-Germain',
            'nationality': 'Argentine',
            'age': '36',
            'position': 'Forward',
            'strong foot': 'Left'
        },
        {
            'name': 'Cristiano Ronaldo',
            'club': 'Manchester United',
            'nationality': 'Portuguese',
            'age': '38',
            'position': 'Forward',
            'strong foot': 'Right'
        },
        {
            'name': 'Neymar Jr',
            'club': 'Paris Saint-Germain',
            'nationality': 'Brazilian',
            'age': '31',
            'position': 'Forward',
            'strong foot': 'Right'
        },
        {
            'name': 'Virgil van Dijk',
            'club': 'Liverpool',
            'nationality': 'Dutch',
            'age': '31',
            'position': 'Defender',
            'strong foot': 'Right'
        },
        {
            'name': 'Kevin De Bruyne',
            'club': 'Manchester City',
            'nationality': 'Belgian',
            'age': '31',
            'position': 'Midfield',
            'strong foot': 'Right'
        },
        {
            'name': 'Kylian Mbappé',
            'club': 'Paris Saint-Germain',
            'nationality': 'French',
            'age': '24',
            'position': 'Forward',
            'strong foot': 'Right'
        },
        {
            'name': 'Mohamed Salah',
            'club': 'Liverpool',
            'nationality': 'Egyptian',
            'age': '30',
            'position': 'Forward',
            'strong foot': 'Left'
        },
        {
            'name': 'Eden Hazard',
            'club': 'Real Madrid',
            'nationality': 'Belgian',
            'age': '32',
            'position': 'Forward',
            'strong foot': 'Right'
        },
        {
            'name': 'Manuel Neuer',
            'club': 'Bayern Munich',
            'nationality': 'German',
            'age': '37',
            'position': 'Goalkeeper',
            'strong foot': 'Right'
        }
    ]
    for item in data:
        if player_name.lower() in item['name'].lower():
            players.append(item)
    return jsonify(players)
        

if __name__ == '__main__':
    app.run(debug=True)

