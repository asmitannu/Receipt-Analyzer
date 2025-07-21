# DATA STORAGE : DATABASE 

import sqlite3

conn = sqlite3.connect("receipts.db", check_same_thread= False)
cursor = conn.cursor()

cursor.execute('''Create table if not exists receipts(id INTEGER PRIMARY KEY, vendor TEXT, date TEXT, amount REAL, currency TEXT, category TEXT) ''')

def insert_data(data):
    cursor.execute('''Insert into receipts (vendor, date, amount, currency, category) values (?,?,?,?,?) ''', (data.vendor, data.date, data.amount, data.currency, data.category))
    
    conn.commit()