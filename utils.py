import csv
import json
from Player import Player
from Table import Table
from Match import Match

def read_matches(filename):
    matches = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
                continue
            player_1 = Player(row[0], row[1])
            player_2 = Player(row[2], row[3])
            table = Table(row[4], row[5])
            match = Match(player_1, player_2)
            match.set_table(table)
            matches.append(match)
            line_count += 1
    return matches

def read_players(filename):
    players = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
                continue
            players.append(Player(row[0], row[1]))
            line_count += 1
    return players

def read_player_history(filename):
    player_history = {}
    with open(filename, newline='') as jsonfile:
        player_history = json.load(jsonfile)
    return player_history

def read_tables(filename):
    tables = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
                continue
            tables.append(Table(row[0], row[1]))
            line_count += 1
    return tables

def write_matches(matches, filename):
    with open(filename, mode='w') as csv_file:
        fieldnames = ['player_1_name', 'player_1_id', 'player_2_name', 'player_2_id', 'table_number', 'terrain_name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for match in matches:
            w_match = {'player_1_name': match.get_players()[0].get_name(), 'player_1_id': match.get_players()[0].get_id(), 'player_2_name': match.get_players()[1].get_name(), 'player_2_id': match.get_players()[1].get_id(), 'table_number': match.get_table().get_table_number(), 'terrain_name': match.get_table().get_terrain_name()}
            writer.writerow(w_match)
