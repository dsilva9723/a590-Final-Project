"""Must put the script in the current working directory
which is open in VS Code
"""
import sqlite3, os
import pandas as pd 

def write_to_json(df, dir, file_name):
    """
    write to JSON, the most popular exchange format on the Web
    """
    fpath = os.path.join(dir, f"{file_name}.json")
    with open(fpath, 'w', encoding='utf-8') as f:
        df.to_json(f, orient="records")

db = sqlite3.connect("redesign/flight2.db") #connect
flights_df = pd.read_sql("select * from flight", db) #run query
print(flights_df) #print
write_to_json(flights_df, "client", "flights") #write to client/flights.json

db.close() #disconnect
