import sqlite3

conn = sqlite3.connect("alumnos.db")
miCursor = conn.cursor()


miCursor.execute('''
    CREATE TABLE Alumnos (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    apellido TEXT
    )
''')

alumnos = [
    (1, "Lionel", "Messi"),
    (2, "Angel", "Di Maria"),
    (3, "Nicolas", "Tagliafico"),
    (4, "Alejandro", "Gomez"),
    (5, "Lautaro", "Martinez"),
    (6, "Alexis", "McAllister"),
    (7, "Emiliano","Martinez"),
    (8, "Enzo", "Fernandez")
]

miCursor.executemany("INSERT INTO Alumnos VALUES (?,?,?)", alumnos)



#Leer/ buscar informacion de la tabla segun nombre.
miCursor.execute("SELECT * FROM alumnos WHERE nombre = 'Lionel' ")

result = miCursor.fetchone()
print(result)


conn.commit()
conn.close()