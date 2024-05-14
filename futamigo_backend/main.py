from flask import Flask, jsonify
import requests
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from db import init_app
from db import db
from models import Player
import random

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://u473184132_admin:420Admin69god!@srv1125.hstgr.io/u473184132_futamigo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_app(app)



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

# @app.route('/futl/<string:player_name>')
# def futl(player_name):
#     players = []
#     data = [
#         {
#             'name': 'Ronaldinho',
#             'club': 'Barcelona',  
#             'nationality': 'Brazilian',
#             'age': '48',
#             'position': 'Midfield',
#             'strong foot': 'Right'
#         },
#         {
#             'name': 'Lionel Messi',
#             'club': 'Paris Saint-Germain',
#             'nationality': 'Argentine',
#             'age': '36',
#             'position': 'Forward',
#             'strong foot': 'Left'
#         },
#         {
#             'name': 'Cristiano Ronaldo',
#             'club': 'Manchester United',
#             'nationality': 'Portuguese',
#             'age': '38',
#             'position': 'Forward',
#             'strong foot': 'Right'
#         },
#         {
#             'name': 'Neymar Jr',
#             'club': 'Paris Saint-Germain',
#             'nationality': 'Brazilian',
#             'age': '31',
#             'position': 'Forward',
#             'strong foot': 'Right'
#         },
#         {
#             'name': 'Virgil van Dijk',
#             'club': 'Liverpool',
#             'nationality': 'Dutch',
#             'age': '31',
#             'position': 'Defender',
#             'strong foot': 'Right'
#         },
#         {
#             'name': 'Kevin De Bruyne',
#             'club': 'Manchester City',
#             'nationality': 'Belgian',
#             'age': '31',
#             'position': 'Midfield',
#             'strong foot': 'Right'
#         },
#         {
#             'name': 'Kylian Mbappé',
#             'club': 'Paris Saint-Germain',
#             'nationality': 'French',
#             'age': '24',
#             'position': 'Forward',
#             'strong foot': 'Right'
#         },
#         {
#             'name': 'Mohamed Salah',
#             'club': 'Liverpool',
#             'nationality': 'Egyptian',
#             'age': '30',
#             'position': 'Forward',
#             'strong foot': 'Left'
#         },
#         {
#             'name': 'Eden Hazard',
#             'club': 'Real Madrid',
#             'nationality': 'Belgian',
#             'age': '32',
#             'position': 'Forward',
#             'strong foot': 'Right'
#         },
#         {
#             'name': 'Manuel Neuer',
#             'club': 'Bayern Munich',
#             'nationality': 'German',
#             'age': '37',
#             'position': 'Goalkeeper',
#             'strong foot': 'Right'
#         }
#     ]
#     for item in data:
#         if player_name.lower() in item['name'].lower():
#             players.append(item)
#     return jsonify(players)

@app.route('/futl/<string:player_name>')
def futl(player_name):
    # Query the database for players whose name contains the provided 'player_name'
    players = Player.query.filter(Player.name.ilike(f'%{player_name}%')).all()

    # Convert the player objects to a list of dictionaries to jsonify
    players_data = [
        {
            'id': player.id,
            'name': player.name,
            'nationality': player.nationality,
            'age': player.age,
            'foot': player.foot,
            'club': player.club,
            'market_value': player.market_value
        } for player in players
    ]

    return jsonify(players_data)


@app.route('/randPlayer')
def randPlayer():
    try:
        player_count = Player.query.count()
        
        if player_count == 0:
            return jsonify({'error': 'No players available'}), 404

        random_index = random.randint(0, player_count - 1)
        
        random_player = Player.query.offset(random_index).first()

        player_data = {
            'id': random_player.id,
            'name': random_player.name,
            'nationality': random_player.nationality,
            'foot': random_player.foot,
            'club': random_player.club,
            'market_value': random_player.market_value
        }
        return jsonify(player_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/add_player')
def add_player():
    # Create a new player instance
    new_player = Player(
        name='Lionel Messi',
        nationality='Argentine',
        age = 36,
        foot='Left',
        club='Paris Saint-Germain',
        market_value=80000000
    )

    # Add the new player to the database session
    db.session.add(new_player)

    # Commit the session to save changes to the database
    db.session.commit()

    return f'Added new player: {new_player.name}'



if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)

