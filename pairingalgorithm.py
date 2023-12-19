import csv
import json
import random
from utils import read_matches, read_players, read_player_history, read_tables
from Player import Player
from Table import Table
from Match import Match

def remove_contradicting_tables(match_tables, player_history):
    possible_matches = match_tables

    for match in match_tables:
        for table in match_tables[match]:
            player1, player2 = match.get_players()

            player1_tables = player_history[player1.get_id()]['tables']
            player2_tables = player_history[player2.get_id()]['tables']
            
            if (table in player1_tables) or (table in player2_tables):
                possible_matches[match].remove(table)

    return possible_matches

def remove_table_from_matches(match_tables, table):
    possible_matches = match_tables

    for match in match_tables:
        if table in match_tables[match]:
            match_tables[match].remove(table)
    return possible_matches

def get_table_pairings(player_filename, player_history_filename, match_filename, table_filename):
    matches = read_matches(match_filename)
    final_matches = []
    tables = read_tables(table_filename)
    players = read_players(player_filename)
    player_history = read_player_history(player_history_filename)

    # Create dictionary of possible matches on each table

    match_tables = {}

    for match in matches:
        match_tables[match] = list([int(t.get_table_number()) for t in tables])

    # Remove tables that contradict player history
    # Assign matches to tables with the least number of possible tables
    # Remove table that has already been assigned

    while match_tables.items():
        match_tables = remove_contradicting_tables(match_tables, player_history)
        minimum_match = min(match_tables, key=lambda x: len(match_tables[x]))
        minimum_match_tables = match_tables.pop(minimum_match)
        chosen_table = random.choice(minimum_match_tables)
        matches.remove(minimum_match)

        minimum_match.set_table(chosen_table)
        final_matches.append(minimum_match)

        match_tables = remove_table_from_matches(match_tables, chosen_table)
    
    print([fm.get_table() for fm in final_matches])


get_table_pairings('players.csv', 'player_history.json', 'matches.csv', 'tables.csv')
