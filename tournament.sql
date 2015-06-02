-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drop, Create and connect to tournament database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Drop players and matches tables if they exists
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS matches;

-- Create new table playes with id and name
CREATE TABLE players (
	id serial primary key,
	name TEXT
	);

-- Create table matches
-- id, primary key of table
-- id_player, reference to table players field id
-- win, counter of victories
-- matches, counter for how many matches he played
CREATE TABLE matches (
	id serial primary key,
	id_player serial references players(id) ON DELETE CASCADE ON UPDATE CASCADE,
	win INT, matches INT
	);
