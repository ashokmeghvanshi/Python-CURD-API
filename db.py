
import sqlite3

conn = sqlite3.connect('GDDatabase.db')
print('Opened Database Successfully')

conn.execute('CREATE TABLE Greendeck (P_ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL,Brand_Name TEXT,Regular_Price FLOAT NOT NULL,Offer_Price FLOAT NOT NULL,Currency TEXT NOT NULL,CL1 TEXT NOT NULL,CL2 TEXT,CL3 TEXT,CL4 TEXT,Image_Url TEXT)')
print('Table Created Successfully')
conn.close()

