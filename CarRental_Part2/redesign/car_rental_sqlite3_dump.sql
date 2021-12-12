CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE carrental (
id integer primary key AUTOINCREMENT,
locationcity text,
locationstate text,
ownerid int,
airportcity text);
CREATE TABLE specs (
id integer primary key autoincrement, 
ownerid int default null, 
rating double default null,
ratedaily int default null,
vehiclemake text,
vehiclemodel text,
vehicletype text,
vehicleyear int default null);
