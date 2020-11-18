import pandas as pd
import sqlite3

# Import CSV
data = pd.read_csv("Greendeck.csv", encoding= 'unicode_escape', header=0)   

# Import Database 
conn = sqlite3.connect('GDDatabase.db')

cursor = conn.cursor()

# Enter Table Name
data.to_sql('Greendeck', conn, if_exists='append', index = False)

conn.commit()
