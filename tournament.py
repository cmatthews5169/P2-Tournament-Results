#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

# Import PostgreSQL adapter
import psycopg2

# Return connection to database "tournament"
def connect():
    return psycopg2.connect("dbname=tournament")

# Delete existing matches
def deleteMatches():
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM matches")
    db.commit()
    db.close()

# Delete existing players
def deletePlayers():
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM players")
    db.commit()
    db.close()

# Count all registered players
def countPlayers():
    db = connect()
    c = db.cursor()
    c.execute("SELECT count(player_id) FROM players")
    player_count = c.fetchall()[0][0]
    db.close()
    return(player_count);

# Register a new player 
def registerPlayer(name):
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO players (player_name) VALUES (%s)",(name,))
    db.commit()
    db.close();

# Return a list of players and win records sorted by wins. 
def playerStandings():
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM player_standings")
    standings = c.fetchall();
    db.close()
    return(standings);

# Records the outcome of a match between two players
def reportMatch(winner, loser):
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)",(winner, loser,))
    db.commit()
    db.close()

# Returns a list of pairs of players for the next round of a match
def swissPairings():
    db = connect()
    c = db.cursor()
    c.execute("SELECT player_id, player_name FROM player_standings;")
    pairing_list = c.fetchall()
    db.close()
    pair = []
    for i in range(0, len(pairing_list), 2):
        next_pair = pairing_list[i][0], pairing_list[i][1], pairing_list[i+1][0], pairing_list[i+1][1]
        pair.append(next_pair)
    return pair
