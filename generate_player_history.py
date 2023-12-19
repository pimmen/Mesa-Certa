import csv
import json
import os.path
from Player import Player
from Table import Table
from Match import Match
from utils import read_matches, read_players

# Read in the matches from the csv file

matches_round1 = read_matches('matches_round4.csv')

# Read in the players from the csv file

players = read_players('players.csv')

# Create a dictionary of players and their match history
if os.path.isfile('player_history.json'):
    with open('player_history.json', newline='') as jsonfile:
        player_history = json.load(jsonfile)
else:
    player_history = {}

for player in players:
    for match in matches_round1:
        if match.player_was_in_match(player):
            player.play_match(match)
    if player.get_id() not in player_history:
        player_history[player.get_id()] = {'tables': [int(t.get_table_number()) for t in player.get_tables()], 
                                         'player_name': player.get_name()}
    else:
        player_history[player.get_id()]['tables'].extend([int(t.get_table_number()) for t in player.get_tables()])

# Write the player history to a json file
    
with open('player_history.json', 'w') as outfile:
    json.dump(player_history, outfile, indent=4)

