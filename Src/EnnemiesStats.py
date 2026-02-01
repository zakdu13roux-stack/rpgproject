"""
Description:
    Accès aux statistiques des ennemis via la base de données.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  database="testosterone"
)
cursor = db.cursor()

def GetDamageDealers():
    """
    Description:
        Donne les ennemis de type Damage Dealer.
    Entrées:
        Aucune.
    Sorties:
        list: lignes de la base de données.
    """
    cursor.execute("Select * From enemies Where Type = 'DamageDealer'")
    return cursor.fetchall()

def GetTanks():
    """
    Description:
        Donne les ennemis de type Tank.
    Entrées:
        Aucune.
    Sorties:
        list: lignes de la base de données.
    """
    cursor.execute("Select * From enemies Where Type = 'Tank'")
    return cursor.fetchall()

def GetSupports():
    """
    Description:
        Donne les ennemis de type Support.
    Entrées:
        Aucune.
    Sorties:
        list: lignes de la base de données.
    """
    cursor.execute("Select * From enemies Where Type = 'Support'")
    return cursor.fetchall()

def GetBoss():
    """
    Description:
        Donne les ennemis de type Boss.
    Entrées:
        Aucune.
    Sorties:
        list: lignes de la base de données.
    """
    cursor.execute("Select * From enemies Where Type = 'Boss'")
    return cursor.fetchall()

def GetEnemyStats(enemy):
    """
    Description:
        Donne toutes les statistiques d'un ennemi.
    Entrées:
        enemy: nom de l'ennemi.
    Sorties:
        tuple: statistiques de l'ennemi.
    """
    cursor.execute(f"Select * From enemies Where Nom = '{enemy}'")
    return cursor.fetchall()[0]

if __name__ == '__main__':
    print(GetDamageDealers())
    print(GetTanks())
    print(GetSupports())
    print(GetBoss())
    print(GetEnemyStats("Gorille"))