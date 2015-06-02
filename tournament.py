#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        DB = psycopg2.connect("dbname={}".format(database_name))
        cursor = DB.cursor()
        return DB, cursor
    except:
        print("Error to connect to database")


def deleteMatches():
    """Remove all the match records from the database."""
    DB, c = connect()
    c.execute("TRUNCATE matches")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB, c = connect()
    c.execute("DELETE FROM players")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB, c = connect()
    c.execute("SELECT COUNT(*) FROM players")
    row = c.fetchone()
    return row[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    DB, c = connect()
    c.execute("INSERT INTO players(name) VALUES (%s)", (name,))
    c.execute("SELECT MAX(id) from players")
    id = c.fetchone()
    c.execute("INSERT INTO matches (id, win, matches) VALUES(%s,%s,%s)", (id[0], 0, 0))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB, c = connect()
    c.execute("SELECT p.id, p.name, m.win, m.matches FROM players p INNER JOIN matches m ON m.id = p.id order by m.win DESC")
    rows = c.fetchall()
    DB.close()
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    DB, c = connect()
    c.execute("UPDATE matches SET win = win+1, matches = matches+1 WHERE id = %s", (winner,))
    c.execute("UPDATE matches SET matches = matches+1 WHERE id = %s", (loser,))
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
        CREATE TABLE players (id serial primary key, name TEXT);
        CREATE TABLE matches (id serial, win INT, matches INT);
    """
    DB, c = connect()
    c.execute("SELECT p.id, p.name FROM players p INNER JOIN matches m ON m.id = p.id order by m.win")
    rows = c.fetchall()
    num = len(rows)
    lista = []
    for i in xrange(0, num, 2):
        lista.append((rows[i]+rows[i+1]))
    DB.close()
    return lista
