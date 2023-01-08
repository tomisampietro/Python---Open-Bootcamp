import sqlite3
import getpass

"""
#CREAR LA BASE DE DATOS Y PASARLE ALGUNOS DATOS
miConexion = sqlite3.connect("users.db")

miCursor = miConexion.cursor()

#Para que la creacion de la PK sea automatica, se agrega el ID
miCursor.execute('''
    CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL)
''')

usuarios = [
    (1, "tomas", "miclave"),
    (2, "martina", "clave"),
]

miCursor.executemany("INSERT INTO users VALUES (?,?,?)", usuarios)

miConexion.commit()
miConexion.close()
"""

def main():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if verifica_credenciales(username, password):
        print("Login approbed")
    else:
        print("Access denied")

def verifica_credenciales(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    print("Query a ejecutar: ", query)
    
    rows = cursor.execute(query)
    data = rows.fetchone()


    cursor.close()
    conn.close()

    if data  == None:
        return False

    return True

if __name__ == "__main__":
    main()


