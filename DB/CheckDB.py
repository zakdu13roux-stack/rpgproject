import mysql.connector
import os

def createDB():
    """
    Supprime la base de données si elle existe, puis la recrée avec les tables.
    """
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")


    dbPresent = False
    for base in mycursor:
        if base[0] == "testosterone":
            dbPresent = True


    if dbPresent:
        mycursor.execute("DROP DATABASE testosterone")
        print("Base de données supprimée.")
    
    
    mycursor.execute("CREATE DATABASE testosterone")
    print("Base de données créée.")
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      database="testosterone"
    )
    mycursor = mydb.cursor()

    with open(os.path.join(os.path.dirname(__file__), 'testosterone.sql'), 'r', encoding='utf-8') as f:
        sql = f.read()
        try:
            # Diviser les requêtes par point-virgule et les exécuter une par une
            for query in sql.split(';'):
                query = query.strip()
                if query:
                    mycursor.execute(query)
            print("Tables créées avec succès.")
        except mysql.connector.Error as e:
            print(f"Erreur lors de l'exécution du script SQL : {e}")
            return False
    
    mydb.commit()
    return False

if __name__ == '__main__':
    result = createDB()
    print("Terminé.")