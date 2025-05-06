# Baseball Stats Tracker - CLI
import json

players = {}

def calculate_stats(data):
    ab = data['at_bats']
    h = data['hits']
    bb = data['walks']
    tb = data['total_bases']
    rbis = data['rbis']
    avg = h / ab if ab else 0
    obp = (h + bb) / (ab + bb) if (ab + bb) else 0
    slg = tb / ab if ab else 0
    return {'AVG': round(avg, 3), 'OBP': round(obp, 3), 'SLG': round(slg, 3), 'RBI': rbis}

def add_player():
    name = input("Name: ")
    players[name] = {'at_bats': 0, 'hits': 0, 'walks': 0, 'total_bases': 0, 'rbis': 0}

def update_stats():
    name = input("Player to update: ")
    ab = int(input("AB: "))
    h = int(input("Hits: "))
    bb = int(input("Walks: "))
    tb = int(input("Total Bases: "))
    rbis = int(input("RBIs: "))
    p = players[name]
    p['at_bats'] += ab
    p['hits'] += h
    p['walks'] += bb
    p['total_bases'] += tb
    p['rbis'] += rbis

def display_stats():
    for name, data in players.items():
        stats = calculate_stats(data)
        print(f"{name}: AVG={stats['AVG']}, OBP={stats['OBP']}, SLG={stats['SLG']}, RBI={stats['RBI']}")

def main():
    while True:
        print("1. Add Player\n2. Update Stats\n3. View Stats\n4. Exit")
        c = input("Choice: ")
        if c == '1': add_player()
        elif c == '2': update_stats()
        elif c == '3': display_stats()
        elif c == '4': break

if __name__ == '__main__':
    main()
