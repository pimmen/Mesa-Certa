import csv
import json
from Player import Player
from Table import Table
from Match import Match
from utils import read_matches, read_players

# Read in the matches from the csv file

matches_round1 = read_matches('matches_round1.csv')

# Read in the players from the csv file

players = read_players('players.csv')

# Create a dictionary of players and their match history

player_history = {}

for player in players:
    for match in matches_round1:
        if match.player_was_in_match(player):
            player.play_match(match)

    player_history[player.get_id()] = {'tables': [int(t.get_table_number()) for t in player.get_tables()], 
                                         'player_name': player.get_name()}

# Write the player history to a json file
    
with open('player_history.json', 'w') as outfile:
    json.dump(player_history, outfile, indent=4)

