import sys, os
# import custom module from a directory 'function'
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from function import config

import pandas as pd
# pip install mysql-connector-python
# pip install pymysql
# pip install sqlalchemy
import mysql.connector as mc
from mysql.connector import errorcode

# make db connection
db = config.connect_mysql("flight")

# transaction
if db is not None:
    #read
    airlines_df = pd.read_sql("select * from airlines", db)    
    airlines_df.info()
    #location: in a subfolder report
    dir = "report" 
    #create subfolder if not exists
    if not os.path.exists(dir): 
        os.mkdir(dir) 
    #write
    file_name = "airlines_list" #filename
    fpath = os.path.join(dir, f"{file_name}.csv")
    with open(fpath, "w", encoding="utf-8" ) as f:
        airlines_df.to_csv(f, index=False, line_terminator='\n')
    #close connection
    db.close()  
else:
    print(f"No connection available.") 
