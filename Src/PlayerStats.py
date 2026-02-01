"""
Description:
    Accès et mise à jour des statistiques du joueur dans la base.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

import mysql.connector
import uuid
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  database="testosterone"
)
cursor = db.cursor()


def get_computer_uuid(curseur):
    """
    Description:
        Récupère ou génère l'UUID unique de la machine.
    Entrées:
        curseur: curseur de la base de données.
    Sorties:
        str: UUID du joueur.
    """
    UUID_FILE = "game_uuid.txt"
    if os.path.exists(UUID_FILE):
        with open(UUID_FILE, "r") as f:
            return f.read().strip()
    else:
        Ids = curseur.execute("Select playerID From players")
        new_uuid = str(uuid.uuid4())
        if Ids != None:
            while new_uuid in Ids:
                new_uuid = str(uuid.uuid4())
        with open(UUID_FILE, "w") as f:
            f.write(new_uuid)
        return new_uuid

uuid = get_computer_uuid(cursor)


def OG(curseur,id):
    """
    Description:
        Vérifie l'existence du joueur et l'enregistre si besoin.
    Entrées:
        curseur: curseur de la base de données.
        id: UUID du joueur.
    Sorties:
        Aucune.
    """
    curseur.execute(f"Select PlayerID From players Where PlayerID = '{id}'")
    if curseur.fetchall() == []:
        SignIn(curseur,id)
        print("Player inserted in database.")
    else:
        print("Player already in database.")

def SignIn(curseur, id):
    """
    Description:
        Enregistre un nouveau joueur dans la base.
    Entrées:
        curseur: curseur de la base de données.
        id: UUID du joueur.
    Sorties:
        Aucune.
    """
    Nom = str()
    MDP = str()
    while len(Nom)<1 or len(Nom)>10:
        Nom = str(input("Quel nom choisissez vous? (Entre 1 et 10 characters) "))
    while len(MDP)<5 or len(MDP)>30:
        MDP = str(input("Votre mot de passe?🤫 (Entre 5 et 30 characters) "))
    curseur.execute(f"Insert Into players (PlayerID,Name,MDP) Values ('{id}','{Nom}','{MDP}')")
    db.commit()

def GetLife():
    """
    Description:
        Donne la vie actuelle du joueur.
    Entrées:
        Aucune.
    Sorties:
        int: points de vie.
    """
    cursor.execute(f"Select Vie From players Where PlayerID = '{uuid}'")
    return cursor.fetchall()[0][0]
def AddLife(vie):
    """
    Description:
        Ajoute de la vie au joueur en base.
    Entrées:
        vie: quantité de vie à ajouter.
    Sorties:
        Aucune.
    """
    cursor.execute(f"Update players Set Vie = Vie+{vie} Where PlayerID = '{uuid}'")
    db.commit()

def GetAtk():
    """
    Description:
        Donne l'attaque de base du joueur.
    Entrées:
        Aucune.
    Sorties:
        int: valeur d'attaque.
    """
    cursor.execute(f"Select AtkDeBase From players Where PlayerID = '{uuid}'")
    return cursor.fetchall()[0][0]
def AddAtk(dg):
    """
    Description:
        Ajoute de l'attaque au joueur en base.
    Entrées:
        dg: quantité d'attaque à ajouter.
    Sorties:
        Aucune.
    """
    cursor.execute(f"Update players Set AtkDeBase = AtkDeBase+{dg} Where PlayerID = '{uuid}'")
    db.commit()

def GetReducDegat():
    """
    Description:
        Donne la réduction de dégâts du joueur.
    Entrées:
        Aucune.
    Sorties:
        int: réduction de dégâts.
    """
    cursor.execute(f"Select ReducDegat From players Where PlayerID = '{uuid}'")
    return cursor.fetchall()[0][0]
def AddReducDegat(dg):
    """
    Description:
        Ajoute une réduction de dégâts en base.
    Entrées:
        dg: quantité de réduction.
    Sorties:
        Aucune.
    """
    cursor.execute(f"Update players Set ReducDegat = ReducDegat+{dg} Where PlayerID = '{uuid}'")
    db.commit()

def GetArgent():
    """
    Description:
        Donne l'argent du joueur.
    Entrées:
        Aucune.
    Sorties:
        int: argent du joueur.
    """
    cursor.execute(f"Select Argent From players Where PlayerID = '{uuid}'")
    return cursor.fetchall()[0][0]
def AddArgent(arg):
    """
    Description:
        Ajoute de l'argent au joueur en base.
    Entrées:
        arg: quantité d'argent.
    Sorties:
        Aucune.
    """
    cursor.execute(f"Update players Set Argent = Argent+{arg} Where PlayerID = '{uuid}'")
    db.commit()

def GetName():
    """
    Description:
        Donne le nom du joueur.
    Entrées:
        Aucune.
    Sorties:
        str: nom du joueur.
    """
    cursor.execute(f"Select Name From players Where PlayerID = '{uuid}'")
    return cursor.fetchall()[0][0]
def ChangeName(name):
    """
    Description:
        Met à jour le nom du joueur en base.
    Entrées:
        name: nouveau nom.
    Sorties:
        Aucune.
    """
    cursor.execute(f"Update players Set Nom = {name} Where PlayerID = '{uuid}'")
    db.commit()

def GetVolume():
    """
    Description:
        Donne le volume enregistré.
    Entrées:
        Aucune.
    Sorties:
        float: volume.
    """
    cursor.execute(f"Select Volume From players Where PlayerID = '{uuid}'")
    return cursor.fetchall()[0][0]
def ChangeVolume(vol):
    """
    Description:
        Met à jour le volume en base.
    Entrées:
        vol: nouveau volume.
    Sorties:
        Aucune.
    """
    cursor.execute(f"Update players Set Volume = {vol} Where PlayerID = '{uuid}'")
    db.commit()


if __name__ == '__main__':
    ChangeVolume(1)
    print(GetVolume())
