import logging
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="examly",  
   
)
cursor = mydb.cursor()
logging.info("root")