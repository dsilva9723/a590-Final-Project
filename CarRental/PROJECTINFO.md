# CarRental Project for A590
**Project Scenario:**
    Phillip, Tyler, Vishnu, and Damian are buisness entrepeneurs and are having a grand opening for used car dealership called "Python Motors". Our mission is to provide
    quality used cars to Northwest Indiana Residents at affordable prices. We pride ourselves on our compettive prices and our variety of financing options. Our team will strive
    to find the right car to meet customer expectations.
    Using our up-to-date database application listing our inventory, we can provide the customer with a quality used car that meets their needs, sold at an affordable price, and
    has a detailed report of attributes on the car. Our team will provide data forecasting to find out what type of cars are selling more frequently throughout each quarter and
    utilize these trends for future car purchases for the dealership.
    
    **How to view our data:**
    
    1) Open CarRental folder in VS code
    
    2) Open subfolder **function** and open file **config.py**.
    
    3) Alter the following in VS code to meet your MySQL Connection preferences:
            mysql_host = "127.0.0.1"
            mysql_user = "root"
            mysql_pwd = "Password"
            #mysql_pwd_mac = ""
            mysql_port = 3306
            #mysql_port_mac = 3306
            
    4) Open MySQL Workbench and run the following SQL script to create a schema for our data insert:
            create schema carrental;
            
    5) Once carrental schema has been inserted in MySQL Workbench, return to CarRental folder in VS code.
    
    6) In subfolder **redesign** open file **carRental_insert.py**.
    
    7) Run **carRental_insert.py** python file.
    
    8) In subfolder **redesign** open file **carSpecs_insert.py**.
    
    9) Run **carSpecs_insert.py** python file.
    
    10) Return to MySQL Workbench. Open carrental schema -> tables -> carspecs. Run the following SQL cript:
             use carrental;
             select *
             from carspecs;
             
    11) Return to MySQL Workbench. Open carrental schema -> tables -> rentlocation. Run the following SQL cript:
             use carrental;
             select *
             from rentlocation;      
     
    12) Celebrate! 
            
           
  
