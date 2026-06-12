import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="foodstreet"
)

cursor = db.cursor()