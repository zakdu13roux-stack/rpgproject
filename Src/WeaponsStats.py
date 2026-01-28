import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  database="testosterone"
)
cursor = db.cursor()

def GetWeapons():
    """
    Donne toutes les armes.
    """
    cursor.execute("Select * From weapons")
    return cursor.fetchall()

def GetPourieWeapons():
    """
    Donne toutes les armes de rareté 'Pourie'.
    """
    cursor.execute("Select * From weapons Where Rarete = 'Pourie'")
    return cursor.fetchall()

def GetOkWeapons():
    """
    Donne toutes les armes de rareté 'Ok'.
    """
    cursor.execute("Select * From weapons Where Rarete = 'Ok'")
    return cursor.fetchall()

def GetLegendaireWeapons():
    """
    Donne toutes les armes de rareté 'Légendaire'.
    """
    cursor.execute("Select * From weapons Where Rarete = 'Légendaire'")
    return cursor.fetchall()


if __name__ == '__main__':
    print(GetWeapons())
    print(GetPourieWeapons())
    print(GetOkWeapons())
    print(GetLegendaireWeapons())