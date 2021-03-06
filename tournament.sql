-- Reset DATABASE
DROP DATABASE tournament;
CREATE DATABASE tournament;

-- Connect to database
\c tournament;

-- Create TABLE players
CREATE TABLE players (
        player_id serial PRIMARY KEY,
        player_name varchar (30) NOT NULL
);

-- Create TABLE matches
CREATE TABLE matches (
        winner INT REFERENCES players(player_id) ON DELETE CASCADE,
        loser INT REFERENCES players(player_id) ON DELETE CASCADE,
        PRIMARY KEY (winner, loser),
        CHECK (winner <> loser)
);

-- Create VIEW player_standings
CREATE VIEW player_standings AS
SELECT players.player_id, players.player_name,
(SELECT count(matches.winner)
    FROM matches
    WHERE players.player_id = matches.winner)
    AS win_total,
(SELECT count(*)
    FROM matches
    WHERE players.player_id = matches.winner
    OR players.player_id = matches.loser)
    AS match_total
FROM players
ORDER BY win_total DESC, match_total DESC;
