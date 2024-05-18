import sqlite3

connection = sqlite3.connect(database='ItStep.db', timeout=5.0)
pointer = connection.cursor()

# pointer.execute("""CREATE TABLE crypto (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, rate REAL)""")

# pointer.execute("INSERT INTO crypto (name, rate) VALUES ('DogeCoin', 0.1554)")
# valuta = ('Etherum', 3.112)
# pointer.execute("INSERT INTO crypto (name, rate) VALUES (?, ?)", valuta)

valutes = [('Etherum', 3.112), ('DogeCoin', 0.1554), ('BitCoin', 67.033)]
pointer.executemany("INSERT INTO crypto (name, rate) VALUES (?, ?)", valutes)

connection.commit()
connection.close()
