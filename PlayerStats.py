import mysql.connector
import uuid
import os
from CheckDB import seeDB

def LookForDB():
    """
    Créer la base de données si elle n'existe pas sinon ne rien faire.
    """
    seeDB()


db = mysql.connector.connect(
  host="localhost",
  user="root",
  database="testosterone"
)
cursor = db.cursor()


def get_computer_uuid(curseur):
    """
    Donne l'UUID déjà enregistré si il y en à déjà un et sinon en créer un jusqu'à qu'il n'y en ai pas d'identique dans la base de données.

    Entrée:
        curseur: La base de données visée
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
    Vérifier si l'utilisateur à déjà joué, sinon lancer l'enregistrement.

    Entrée:
        curseur: La base de données visée
        id: L'UUID enregistrée plus tôt
    """
    curseur.execute(f"Select PlayerID From players Where PlayerID = '{id}'")
    if curseur.fetchall() == []:
        SignIn(curseur,id)
        print("Player inserted in database.")
    else:
        print("Player already in database.")

def SignIn(curseur, id):
    """
    S'enregistrer dans la base de données en choisissant un nom et un mot de passe.

    Entrée:
        curseur: La base de données visée
        id: L'UUID enregistrée plus tôt
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
    Donne la vie du joueur.
    """
    cursor.execute(f"Select Vie From players Where PlayerID = '{uuid}'")
    return cursor.fetchall()[0][0]

def GetAtk():
    """
    Donne l'attaque du joueur.
    """
    cursor.execute(f"Select AtkDeBase From players Where PlayerID = '{uuid}'")
    return cursor.fetchall()[0][0]

def GetReducDegat():
    """
    Donne la réduction des dégâts du joueur.
    """
    cursor.execute(f"Select ReducDegat From players Where PlayerID = '{uuid}'")
    return cursor.fetchall()[0][0]

def GetArgent():
    """
    Donne l'argent du joueur.
    """
    cursor.execute(f"Select Argent From players Where PlayerID = '{uuid}'")
    return cursor.fetchall()[0][0]

def GetName():
    """
    Donne le nom du joueur.
    """
    cursor.execute(f"Select Name From players Where PlayerID = '{uuid}'")
    return cursor.fetchall()[0][0]

if __name__ == '__main__':
    print(GetName())