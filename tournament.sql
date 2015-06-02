-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament


DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS matches;


CREATE TABLE players (
	id serial primary key,
	name TEXT
	);

CREATE TABLE matches (
	id serial primary key,
	id_player serial references players(id) ON DELETE CASCADE ON UPDATE CASCADE,
	win INT, matches INT
	);
