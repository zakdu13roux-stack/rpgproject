import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  database="testosterone"
)
cursor = db.cursor()

def GetDamageDealers():
    """
    Donne tout les ennemies et leurs statistiques du type 'Damage Dealer'.
    """
    cursor.execute("Select * From enemies Where Type = 'DamageDealer'")
    return cursor.fetchall()

def GetTanks():
    """
    Donne tout les ennemies et leurs statistiques du type 'Tank'.
    """
    cursor.execute("Select * From enemies Where Type = 'Tank'")
    return cursor.fetchall()

def GetSupports():
    """
    Donne tout les ennemies et leurs statistiques du type 'Support'.
    """
    cursor.execute("Select * From enemies Where Type = 'Support'")
    return cursor.fetchall()

def GetEnemyStats(enemy):
    """
    Donne toutes les statistiques (nom, type, atout) de l'ennemie donné.

    Entrée:
        enemy: le nom de l'ennemie
    """
    cursor.execute(f"Select * From enemies Where Nom = '{enemy}'")
    return cursor.fetchall()[0]

if __name__ == '__main__':
    print(GetDamageDealers())
    print(GetTanks())
    print(GetSupports())
    print(GetEnemyStats("Gorille"))