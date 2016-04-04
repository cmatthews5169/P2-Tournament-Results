#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

# Import PostgreSQL adapter
import psycopg2

# Return connection to database "tournament"
def connect(database_name="tournament"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Could not create a connection to the database.")

# Delete existing matches
def deleteMatches():
    db, cursor = connect()
    cursor.execute("DELETE FROM matches")
    db.commit()
    db.close()

# Delete existing players
def deletePlayers():
    db, cursor = connect()
    cursor.execute("DELETE FROM players")
    db.commit()
    db.close()

# Count all registered players
def countPlayers():
    db, cursor = connect()
    cursor.execute("SELECT count(player_id) FROM players")
    player_count = cursor.fetchone()[0]
    db.close()
    return(player_count);

# Register a new player 
def registerPlayer(name):
    db, cursor = connect()
    cursor.execute("INSERT INTO players (player_name) VALUES (%s)",(name,))
    db.commit()
    db.close();

# Return a list of players and win records sorted by wins. 
def playerStandings():
    db, cursor = connect()
    cursor.execute("SELECT * FROM player_standings")
    standings = cursor.fetchall();
    db.close()
    return(standings);

# Records the outcome of a match between two players
def reportMatch(winner, loser):
    db, cursor = connect()
    cursor.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)",(winner, loser,))
    db.commit()
    db.close()

# Returns a list of pairs of players for the next round of a match
def swissPairings():
    pairing_list = playerStandings()
    pair = []
    if (len(pairing_list) % 2 == 0):
        for i in range(0, len(pairing_list), 2):
            next_pair = pairing_list[i][0], pairing_list[i][1], pairing_list[i+1][0], pairing_list[i+1][1]
            pair.append(next_pair)
    return pair
