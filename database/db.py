import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="Foodstreet"
)

cursor = db.cursor()