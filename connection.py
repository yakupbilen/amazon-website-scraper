import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "sample.db")

connection = sqlite3.connect(db_path)

cursor = connection.cursor()
"""

import pyodbc

connection =pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8KK9LII\SQLEXPRESS;DATABASE=sample;UID=sa;PWD=mssql12')

cursor = connection.cursor()
"""