"""
Description:
    Accès aux statistiques des armes via la base de données.
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

def GetWeapons():
    """
    Description:
        Donne toutes les armes.
    Entrées:
        Aucune.
    Sorties:
        list: lignes de la base de données.
    """
    cursor.execute("Select * From weapons")
    return cursor.fetchall()

def GetPourrieWeapons():
    """
    Description:
        Donne les armes de rareté Pourrie.
    Entrées:
        Aucune.
    Sorties:
        list: lignes de la base de données.
    """
    cursor.execute("Select * From weapons Where Rarete = 'Pourrie'")
    return cursor.fetchall()

def GetOkWeapons():
    """
    Description:
        Donne les armes de rareté Ok.
    Entrées:
        Aucune.
    Sorties:
        list: lignes de la base de données.
    """
    cursor.execute("Select * From weapons Where Rarete = 'Ok'")
    return cursor.fetchall()

def GetLegendaireWeapons():
    """
    Description:
        Donne les armes de rareté Légendaire.
    Entrées:
        Aucune.
    Sorties:
        list: lignes de la base de données.
    """
    cursor.execute("Select * From weapons Where Rarete = 'Légendaire'")
    return cursor.fetchall()


if __name__ == '__main__':
    print(GetWeapons())
    print(GetPourieWeapons())
    print(GetOkWeapons())
    print(GetLegendaireWeapons())