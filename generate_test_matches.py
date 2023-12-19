import csv
import random
from Player import Player
from Table import Table
from Match import Match
from utils import read_players

# Read in the players from the csv file
players = read_players('players.csv')

matches = []
num_matches = len(players) // 2

# Create the matches
for i in range(0, num_matches):
    player_1 = random.choice(players)
    players.remove(player_1)
    player_2 = random.choice(players)
    players.remove(player_2)
    matches.append(Match(player_1, player_2))

tournament_tables = []
terrain_names = ['Nachmund','Octarius','Into the Dark','Morloch']

for i in range(0,15):
    tournament_tables.append(Table(i, terrain_names[i%4]))

# Write tables to csv file

with open('tables.csv', mode='w') as csv_file:
    fieldnames = ['table_number', 'terrain_name']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for table in tournament_tables:
        writer.writerow({'table_number': table.get_table_number(), 'terrain_name': table.get_terrain_name()})

for match in matches:
    match.set_table(random.choice(tournament_tables))
    tournament_tables.remove(match.get_table())
    match.match_played()

# Write the matches to a csv file

with open('matches_round3.csv', mode='w') as csv_file:
    fieldnames = ['player_1_name', 'player_1_id', 'player_2_name', 'player_2_id', 'table_number', 'terrain_name']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for match in matches:
        writer.writerow({'player_1_name': match.get_players()[0].get_name(), 'player_1_id': match.get_players()[0].get_id(), 'player_2_name': match.get_players()[1].get_name(), 'player_2_id': match.get_players()[1].get_id(), 'table_number': match.get_table().get_table_number(), 'terrain_name': match.get_table().get_terrain_name()})
