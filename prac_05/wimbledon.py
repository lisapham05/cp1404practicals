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

