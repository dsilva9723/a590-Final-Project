import sys, os
# import module from function directory
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from function import config

import pandas as pd
# pip install mysql-connector-python
# pip install pymysql
# pip install sqlalchemy
from sqlalchemy import create_engine, types

# make a connection to mysql database `flight2`
engine = config.sqlalchemy_mysql("carrental")

# query
if engine is not None:
    #read
    db = engine.connect()
    df = pd.read_sql("select * from carspecs", db)    
    df.info()
    #location: in a subfolder report
    dir = "report" 
    #create subfolder if not exists
    if not os.path.exists(dir): 
        os.mkdir(dir) 
    #write
    file_name = "carspecs_list" #filename
    fpath = os.path.join(dir, f"{file_name}.csv")
    with open(fpath, "w", encoding="utf-8" ) as f:
        df.to_csv(f, index=False, line_terminator='\n')
    #close connection
    db.close()  
else:
    print(f"No connection available.")
