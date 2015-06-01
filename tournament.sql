-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS games;
CREATE TABLE players (id serial primary key, name TEXT);
CREATE TABLE matches (id serial, win INT, matches INT);
CREATE TABLE games (id serial, idA serial, idB serial, win serial);
