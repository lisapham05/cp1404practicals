"""
Wimbledon Winners Data Processor
Estimated time:
Actual time:
"""

FILENAME = 'wimbledon.csv'

def read_wimbledon_data(filename):
    with open(FILENAME, 'r', encoding='utf-8-sig') as in_file:
       data = [line.strip().split(',') for line in in_file]
    return data

def count_champions(data):
    champions_to_wins = {}
    for row in data:
        champion = row[2]
        if champion in champions_to_wins:
            champions_to_wins[champion] += 1
        else:
            champions_to_wins[champion] = 1
    return champions_to_wins
