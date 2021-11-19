-- Create airports table;Do one insert into; import the rest from CSV;
CREATE TABLE IF NOT EXISTS "airports" (
  faa TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  tzone TEXT NOT NULL
);

-- View schema (table structure)
.schema airports

-- INSERT INTO
insert into airports
   (faa, name, tzone)
   values
   ("DFW", "Dallas Fort Worth Intl", "American/Chicago")
   ;

-- List all airports   
.mode markdown
SELECT * FROM airports;

-- Insert the rest airports
-- Write INSERT INTO 

-- Import the rest airports
.mode csv 
.import airports.csv airports --skip 2
.mode markdown
SELECT * FROM airports;

-- Create airlines table
CREATE TABLE airlines (
carrier text primary key,
name text not null
);

.mode csv
.import airlines.csv airlines --skip 1
.mode markdown
select * from airlines;


-- Create flights table
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL,
    FOREIGN KEY(origin) references airports(faa),
    FOREIGN KEY(destination) references airports(faa)
);

-- SQLite view schema
.schema flights



-- Inserts
INSERT INTO flights (origin, destination, duration) VALUES ("DFW", "ORD", 165);

-- SQLite run SQLs in a script; add more flights
.read flights_insert.sql
/*
INSERT INTO flights (origin, destination, duration) VALUES ("EWR", "IAH", 227);
INSERT INTO flights (origin, destination, duration) VALUES ("JFK", "MIA", 160);
INSERT INTO flights (origin, destination, duration) VALUES ("JFK", "BQN", 183);
INSERT INTO flights (origin, destination, duration) VALUES ("EWR", "ORD", 150);
INSERT INTO flights (origin, destination, duration) VALUES ("EWR", "FLL", 158);
INSERT INTO flights (origin, destination, duration) VALUES ("LGA", "DFW", 257);
*/

-- Selects
SELECT * FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin = "JFK";
SELECT * FROM flights WHERE duration > 200;
SELECT * FROM flights WHERE duration > 200 AND destination = "DFW";
SELECT * FROM flights WHERE duration > 200 OR destination = "IAH";
SELECT * FROM flights WHERE origin IN ("EWR", "LGA");
SELECT * FROM flights WHERE origin LIKE "%w%";

-- Update
UPDATE flights SET duration = 160 WHERE origin = "EWR" AND destination = "FLL";

-- Delete
DELETE FROM flights WHERE destination = "FLL";




-- Join
SELECT f.*, a1.faa, a1.name, a2.faa, a2.name
FROM flights f JOIN airports a1 ON f.origin = a1.faa 
    JOIN airports a2 ON f.destination = a2.faa
;

SELECT f.id, f.origin, a1.name as dep_airport, f.destination, a2.name as arr_airport, f.duration
FROM flights f JOIN airports a1 ON f.origin = a1.faa 
    JOIN airports a2 ON f.destination = a2.faa
;


-- Create Passengers table
-- id, firstname, lastname, flight_id

-- Add passengers 

-- Join
SELECT first, origin, destination FROM flights JOIN passengers ON passengers.flight_id = flights.id;

