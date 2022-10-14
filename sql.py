import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    
    c.execute('CREATE TABLE IF NOT EXISTS posts(Name TEXT, Role TEXT, Salary INT)')
    c.execute('INSERT INTO posts VALUES ("Rolf", "Software Engineer", "42000")')
    c.execute('INSERT INTO posts VALUES ("Anna", "Engineer", "21423")')
    c.execute('INSERT INTO posts VALUES ("Bob", "Developer", "5667")')
    
    c.execute('CREATE TABLE IF NOT EXISTS items(Name TEXT, Price INT)')
    c.execute('INSERT INTO items VALUES ("Flower", "25")')
    c.execute('INSERT INTO items VALUES ("Bread", "5")')
    c.execute('INSERT INTO items VALUES ("Chair", "30")')
    
    c.execute('CREATE TABLE IF NOT EXISTS locations(Name TEXT, Size INT, City TEXT)')
    c.execute('INSERT INTO locations VALUES ("Sibiu fct", "2000", "Sibiu")')
    c.execute('INSERT INTO locations VALUES ("Cluj fct", "30000", "Cluj")')
    c.execute('INSERT INTO locations VALUES ("SRL", "1000", "Bucuresti")')