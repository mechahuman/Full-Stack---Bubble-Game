from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB setup with debug logging
try:
    client = MongoClient('mongodb://localhost:27017/')
    # Test the connection
    client.server_info()
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    exit(1)

db = client['bubblegame']
players_collection = db['players']

# Print current collection contents on startup
print("\nCurrent players in database:")
for player in players_collection.find():
    print(player)

@app.route('/api/register/', methods=['POST'])
def register_player():
    data = request.get_json()
    username = data.get('username')
    
    if not username:
        return jsonify({
            'status': 'error',
            'message': 'Username is required'
        }), 400
    
    # Check if player exists
    existing_player = players_collection.find_one({'username': username})
    if existing_player:
        is_new = False
    else:
        # Create new player
        players_collection.insert_one({
            'username': username,
            'highscore': 0
        })
        is_new = True
        print(f"\nNew player registered: {username}")
    
    player = players_collection.find_one({'username': username})
    return jsonify({
        'status': 'success',
        'player': {
            'username': player['username'],
            'highscore': player['highscore'],
            'is_new': is_new
        }
    })

@app.route('/api/update-highscore/', methods=['POST'])
def update_highscore():
    data = request.get_json()
    username = data.get('username')
    score = data.get('score')
    
    if not username or score is None:
        return jsonify({
            'status': 'error',
            'message': 'Username and score are required'
        }), 400
    
    player = players_collection.find_one({'username': username})
    if not player:
        return jsonify({
            'status': 'error',
            'message': 'Player not found'
        }), 404
    
    if score > player['highscore']:
        players_collection.update_one(
            {'username': username},
            {'$set': {'highscore': score}}
        )
        player['highscore'] = score
        print(f"\nUpdated highscore for {username}: {score}")
    
    return jsonify({
        'status': 'success',
        'player': {
            'username': player['username'],
            'highscore': player['highscore']
        }
    })

@app.route('/api/player/<username>/', methods=['GET'])
def get_player(username):
    player = players_collection.find_one({'username': username})
    if not player:
        return jsonify({
            'status': 'error',
            'message': 'Player not found'
        }), 404
    
    return jsonify({
        'status': 'success',
        'player': {
            'username': player['username'],
            'highscore': player['highscore']
        }
    })

@app.route('/api/all/', methods=['GET'])
def get_all_players():
    players = list(players_collection.find().sort('highscore', -1))
    return jsonify({
        'status': 'success',
        'players': [
            {
                'username': player['username'],
                'highscore': player['highscore']
            }
            for player in players
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, port=8000) 