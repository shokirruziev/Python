import sqlite3

conn = sqlite3.connect("star_trek.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

characters = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", characters)

cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))

cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
results = cursor.fetchall()

for row in results:
    print(row)

conn.commit()
conn.close()
