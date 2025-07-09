import mysql.connector

mydb = mysql.connector.connect(
    host="localhost:portnumber",
    user="nitin",
    password="pss",
    database = "nitin"
)

prit(mydb)