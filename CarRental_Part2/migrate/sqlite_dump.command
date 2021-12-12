Render database content to a sql script:
sqlite3 flight_db .dump > flight_dump.sql
Replica:
cat flight_dump.sql | sqlite3 flight_replica.db
