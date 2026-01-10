import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  database="testosterone"
)
cursor = db.cursor()

def __GetDamageDealers__(curseur):
    curseur.execute("Select * From enemies Where Type = 'DamageDealer'")
    return curseur.fetchall()
def GetDamageDealers():
    """
    Donne tout les ennemies et leurs statistiques du type 'Damage Dealer'.
    """
    return __GetDamageDealers__(cursor)

def __GetTanks__(curseur):
    curseur.execute("Select * From enemies Where Type = 'Tank'")
    return curseur.fetchall()
def GetTanks():
    """
    Donne tout les ennemies et leurs statistiques du type 'Tank'.
    """
    return __GetTanks__(cursor)

def __GetSupports__(curseur):
    curseur.execute("Select * From enemies Where Type = 'Support'")
    return curseur.fetchall()
def GetSupports():
    """
    Donne tout les ennemies et leurs statistiques du type 'Support'.
    """
    return __GetSupports__(cursor)

if __name__ == '__main__':
    print(GetDamageDealers())
    print(GetTanks())
    print(GetSupports())