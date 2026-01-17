import mysql.connector
def seeDB():
    """
    Créer la base de données si elle n'existe pas et renvoie 'False', sinon renvoie 'True.
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
        return True
    else:
        mycursor.execute("CREATE DATABASE testosterone")
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          database="testosterone"
        )
        mycursor = mydb.cursor()

        f = open('testosterone.sql', 'r')
        mycursor.execute(" ".join(f.readlines()))
        f.close()
        return False