import json
from pymongo import MongoClient
import os

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['bubblegame']
players_collection = db['players']

# Load existing players from JSON
def load_players():
    if os.path.exists('players.json'):
        with open('players.json', 'r') as f:
            return json.load(f)
    return {}

# Migrate data
players = load_players()
for username, data in players.items():
    players_collection.update_one(
        {'username': username},
        {'$set': {'highscore': data['highscore']}},
        upsert=True
    )

print("Migration completed successfully!") 