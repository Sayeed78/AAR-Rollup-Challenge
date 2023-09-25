# This file creates a database connection using python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Sohail Sayeed Local",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")