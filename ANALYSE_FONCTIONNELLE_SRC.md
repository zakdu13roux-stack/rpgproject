# Analyse Fonctionnelle des Fichiers du Dossier Src

**Projet :** RPG Project (Jeu de Rôle)  
**Date :** Février 2026  
**Structure :** Jeu basé sur la librairie Arcade (Python)

---

## 📋 Table des matières

1. [Fichiers de Gestion de Données](#gestion-de-données)
2. [Fichiers de Joueur](#fichiers-de-joueur)
3. [Fichiers d'Ennemis](#fichiers-dennemis)
4. [Fichiers de Système de Combat](#système-de-combat)
5. [Fichiers de Vues (UI)](#fichiers-de-vues-ui)
6. [Fichiers d'Animations et Utilitaires](#animations-et-utilitaires)
7. [Dossier DB - Base de Données](#dossier-db---base-de-données)
8. [Structure Générale du Jeu](#structure-générale)

---

## 🗄️ Gestion de Données

### **PlayerStats.py**
**Objectif :** Accès et gestion des statistiques du joueur dans la base de données MySQL

**Fonctionnalités principales :**
- Connexion à la base de données "testosterone"
- Génération et gestion de l'UUID unique de la machine (stocké dans `game_uuid.txt`)
- Enregistrement automatique d'un nouveau joueur ou validation de l'existence
- **Fonctions principales :**
  - `get_computer_uuid()` : Récupère ou génère l'UUID du joueur
  - `OG()` : Vérifie l'existence du joueur
  - `SignIn()` : Enregistre un nouveau joueur avec nom et mot de passe
  - `GetLife()` : Récupère les points de vie actuels
  - `GetAtk()` : Obtient la valeur d'attaque
  - `GetReducDegat()` : Récupère la réduction de dégâts
  - `GetName()` : Récupère le nom du joueur
  - `GetItems()` : Récupère l'inventaire du joueur
  - `GetArgent()` : Obtient l'argent du joueur
  - Fonctions d'ajout : `AddLife()`, `AddArgent()`, etc.

**État :** ✅ Produit (utilisé par tous les modules)

---

### **WeaponsStats.py**
**Objectif :** Accès aux statistiques des armes depuis la base de données

**Fonctionnalités principales :**
- Récupération des armes par rareté
- Requêtes SQL pour filtrer les armes

**Fonctions principales :**
- `GetWeapons()` : Toutes les armes
- `GetPourrieWeapons()` : Armes de rareté "Pourrie"
- `GetOkWeapons()` : Armes de rareté "Ok"
- `GetLegendaireWeapons()` : Armes de rareté "Légendaire"

**État :** ✅ Produit

---

### **EnnemiesStats.py**
**Objectif :** Accès aux statistiques des ennemis par type

**Fonctionnalités principales :**
- Récupération des ennemis filtrés par classe
- Requêtes SQL catégorisées

**Fonctions principales :**
- `GetDamageDealers()` : Ennemis DamageDealer
- `GetTanks()` : Ennemis Tank (défenseurs)
- `GetSupports()` : Ennemis Support (guérisseurs)
- `GetBoss()` : Ennemis Boss
- `GetEnemyStats()` : Statistiques d'un ennemi spécifique

**État :** ✅ Produit

---

## 👤 Fichiers de Joueur

### **PlayerInGame.py**
**Objectif :** Représentation et gestion du joueur pendant le jeu

**Classe :** `player`

**Attributs :**
- `maxVie` : Points de vie maximum
- `vie` : Points de vie actuels
- `attaque` : Valeur d'attaque
- `ReducDegat` : Réduction de dégâts
- `Name` : Nom du joueur
- `sac` : Inventaire (matrice 2x3)

**Méthodes principales :**
- `takeDamage(dmg)` : Applique des dégâts au joueur
- `heal(health)` : Soigne le joueur
- `GetPlayerStats()` : Retourne (maxVie, vie, attaque, ReducDegat)
- `GetPlayerWeapons()` : Retourne l'inventaire

**État :** ✅ Produit

---

## 🧟 Fichiers d'Ennemis

### **Ennemies.py**
**Objectif :** Définition et génération aléatoire des ennemis selon la difficulté

**Classe :** `Ennemi`

**Système de génération :**
- **Types d'ennemis :** Tank, Damage Dealer, Support (+ Boss)
- **Statistiques :**
  - Vie basée sur la difficulté + valeurs aléatoires
  - Attaque basée sur celle du joueur (½ réduction max)
  - Chaque type a des statistiques différentes

**Méthodes principales :**
- `ennemi_aléatoire()` : Génère un ennemi aléatoire selon le type
- `Random_Damage_Dealer()` : Sélectionne un DamageDealer
- `Random_Tank()` : Sélectionne un Tank
- `Random_Support()` : Sélectionne un Support
- `Random_Boss()` : Sélectionne un Boss

**État :** ✅ Produit

---

### **EnnemiesInGame.py**
**Objectif :** Gestion des ennemis actifs pendant le combat

**Classe :** `SetUpEnemy`

**Fonctionnalités :**
- Initialisation d'une liste d'ennemis pour un combat
- Gestion de plusieurs ennemis avec dictionnaire interne
- Format : `{index: [nom, maxVie, vieActuelle, attaque]}`

**Méthodes principales :**
- `dealDamage(enemy, dmg)` : Applique des dégâts à un ennemi
- `Heal(enemy, health)` : Soigne un ennemi
- `GetEnnemieStats(enemy)` : Récupère les stats d'un ennemi
- `GetAllEnnemies()` : Retourne tous les ennemis
- `GetNbEnnemies()` : Compte le nombre d'ennemis

**État :** ✅ Produit

---

## ⚔️ Système de Combat

### **Weapons.py**
**Objectif :** Implémentation des attaques d'armes et application des dégâts

**Armes implémentées :**
1. **Branche** : 10 points de dégâts base
2. **Banane** : 7 points + 7 soins (effet unique)
3. **Hache de Fer** : 32 points (forte)
4. **Épée Rouillée** : 17 points
5. **Lance** : 30 points
6. **Toile** : 11 points

**Système de dégâts :**
- Chaque arme a une fonction qui applique des dégâts multiplié par le bonus d'attaque
- Distinction entre attaques du joueur et des ennemis

**Fonctions principales :**
- `branche(type, target, mul)` : Applique les dégâts de branche
- `H2F()`, `epeeRouille()`, `toile()`, `lance()`, `banane()` : Autres armes

**État :** ✅ Produit

---

### **FightScene.py**
**Objectif :** Vue de combat standard contre plusieurs ennemis

**Classe :** `FightScene` (hérite de `arcade.View`)

**Fonctionnalités :**
- Interface de combat en temps réel
- Affichage du joueur et des ennemis (jusqu'à 3)
- Barres de vie visuelles
- Musique de combat (musicfight.mp3)
- Sélection de cible avec souris
- Système de tour (joueur → ennemis)
- Gestion de la victoire

**Éléments visuels :**
- Sprites d'herbe et chemins (décor)
- Barres de santé pour chaque combattant
- Sprites des ennemis (Singe, Araignée, Gorille, Oazo, Gro-oazo, Ours)

**État :** ✅ Produit

---

### **BossFight.py**
**Objectif :** Vue de combat spécialisée contre un boss unique

**Classe :** `BossFight` (hérite de `arcade.View`)

**Différences avec FightScene :**
- Un seul ennemi (le boss)
- Interface d'attaque spécialisée
- Barre de vie verte pour le boss
- Système de tours identique

**État :** ✅ Produit

---

## 🎮 Fichiers de Vues (UI)

### **Spawn.py**
**Objectif :** Zone de départ / Hub du jeu

**Classe :** `Spawn` (hérite de `arcade.View`)

**Éléments :**
- Sprite du joueur (déplaçable avec Z/Q/S/D)
- Shop (petit bâtiment interactif)
- Portail vers la carte (transition au prochain niveau)
- Gear (icône d'options)
- Herbe et chemins (décor)
- Son des pas (pas.wav)

**Mécaniques :**
- Déplacement du joueur avec les touches ZQSD
- Collision avec le shop → accès à `ShopView()`
- Collision avec le portail → accès à `Map()` ou `MapBoss()`
- Retour à Spawn après mort

**État :** ✅ Produit

---

### **Map.py**
**Objectif :** Carte de progression avec niveaux et sélection

**Classe :** `Map` (hérite de `arcade.View`)

**Fonctionnalités :**
- Affichage de la progression (nombre de cartes complétées)
- Position du joueur sur la carte (4 positions possibles)
- Icônes de niveaux (départ, combat, area, boss, fin)
- Appui sur ENTER pour lancer un niveau

**Logique de progression :**
- Niveau 0 : Combat normal
- Niveau 1 : Combat normal
- Niveau 2 : Combats
- Niveaux multiples de 10 : Boss

**État :** ✅ Produit

---

### **MapBoss.py**
**Objectif :** Variante de la carte pour les combats de boss

**Classe :** `MapBoss` (hérite de `arcade.View`)

**Structure :**
- Identique à `Map.py` mais sans les niveaux optionnels
- Chemin direct vers le boss (4 niveaux au lieu de 3)
- Icône de boss au lieu de fin normal

**État :** ✅ Produit

---

### **ShopView.py**
**Objectif :** Boutique pour améliorer le joueur

**Classe :** `ShopView` (hérite de `arcade.View`)

**Articles disponibles :**
1. **Potion de Vie** : +50 PV, coût = PVActuels + 50
2. **Armes Meilleures** : Ouvre `WeaponShop()` (détail non fourni ici)

**Mécanique :**
- Vérification de l'argent avant achat
- Mise à jour des stats après achat
- Sprites des items affichés

**État :** ✅ Partiellement complet (WeaponShop non implémentée)

---

### **StatueView.py**
**Objectif :** Écran de récompense après un niveau bonus

**Classe :** `StatueView` (hérite de `arcade.View`)

**Choix de récompense :**
- **Vie** : +25% des PV max
- **Pièces** : +argent (montant non spécifié)

**Décor :**
- Statue comme élément central
- Église en arrière-plan

**État :** ✅ Produit

---

### **Menu.py**
**Objectif :** Menu principal avec options et affichage des contrôles

**Classe :** `MenuView` (hérite de `arcade.View`)

**Fonctionnalités :**
- Bouton "Return to Game" → retour à `Spawn()`
- Bouton "Options" → accès à `Options()`
- Affichage des commandes (Z/Q/S/D, Shop, Portail)
- UI organisée en grille

**État :** ✅ Options non complètement implémentées

---

### **Main.py**
**Objectif :** Vue de titre/lancement du jeu

**Classe :** `main` (hérite de `arcade.View`)

**Éléments :**
- Image de titre (TITLE.png)
- Bouton "Play" qui lance le jeu (`Spawn()`)

**État :** ✅ Produit

---

### **Bonus_lvl.py**
**Objectif :** Niveau bonus avec statue et récompense

**Classe :** `Bonus_lvl` (hérite de `arcade.View`)

**Fonctionnalités :**
- Sprite du joueur (déplaçable)
- Statue au centre (collision pour récompense)
- Décor avec sol
- Transition vers `StatueView()`

**État :** ✅ Produit

---

## 🎬 Animations et Utilitaires

### **Animations.py**
**Objectif :** Gestion des animations d'attaque

**Variables globales :**
- `isPlayer` : Indique si l'attaquant est le joueur
- `numero` : Index de la cible
- `sprite_ref` : Sprite de l'attaquant
- `userStats` : Statistiques de l'attaquant
- `Target` : Cible de l'attaque
- `arme` : Type d'arme utilisée

**Fonctions principales :**
- `UseWeapon()` : Exécute l'attaque avec l'arme sélectionnée
- `Attaquer(user, target, weapon, num)` : Initialise l'attaque
- `Move1(delta_time)` : Première phase d'animation (cri et strafe)

**Animation :**
- Planifiée avec `arcade.schedule()`
- Phase 1 : Cri et déplacement de l'attaquant

**État :** ✅ Produit

---

### **CombatSystemExample.py**
**Objectif :** Exemple de système de combat en console

**Fonction :** `Start()`

**Logique :**
- Crée un joueur et des ennemis
- Simule un combat au tour par tour
- Tour 0 : Attaque du joueur
- Tour 1 : Attaques des ennemis
- Boucle jusqu'à mort du joueur ou des ennemis

**État :** 📚 Exemple/Test (non utilisé en jeu)

---

### **User Input Handling.py**
**Objectif :** Exemple de gestion des entrées clavier

**Fonctions :**
- `on_key_press()` : Affiche la touche pressée
- `on_key_release()` : Affiche la touche relâchée

**État :** 📚 Exemple (modèle pour implémentation)

---

## 📚 Fichiers Auxiliaires

### **__init__.py**
**État :** ✅ Vide (initialisation du package)

---

### **game_uuid.txt** et **Main.spec**, **pyinstaller**
**État :** 🔧 Configuration et compilation

---

## 🗄️ Dossier DB - Base de Données

### **CheckDB.py**
**Objectif :** Initialisation et gestion de la base de données MySQL

**Fonction principale :** `createDB()`

**Processus :**
1. Connexion à MySQL Server (localhost, user: root)
2. Vérification de l'existence de la base "testosterone"
3. **Si elle existe :** Suppression complète (`DROP DATABASE`)
4. **Création nouvelle :** `CREATE DATABASE testosterone`
5. **Exécution du script SQL :** Lecture et exécution de `testosterone.sql`
6. Validation des tables créées avec succès

**Fonctionnalités :**
- Reconnexion à la BD fraîchement créée
- Parsing des requêtes SQL (division par `;`)
- Gestion des erreurs MySQL
- Affichage de messages de progression

**Utilisation :** Permet de reset complètement la BD et la repeupler avec les données initiales

**État :** ✅ Utilitaire fonctionnel

---

### **testosterone.sql**
**Objectif :** Script de création complète de la base de données

**Information du serveur :**
- Version MariaDB : 10.4.28
- Version PHP PhpMyAdmin : 8.2.4
- Généré le : 02 février 2026

**Tables créées :**

#### **Table `enemies`**
Référence tous les types d'ennemis du jeu

| Colonne | Type | Description |
|---------|------|-------------|
| `Nom` | VARCHAR(20) | Identificateur unique (PRIMARY KEY) |
| `Type` | VARCHAR(20) | Classe de l'ennemi : Tank, DamageDealer, Support, Boss |
| `Atout` | VARCHAR(20) | Capacité spéciale (ex: "Poison" pour Araignée) |

**Ennemis référencés (7 total) :**
- **Tank :** Gorille, Ours
- **DamageDealer :** Singe, Gro-oazo
- **Support :** Araignée (Poison), Oazo
- **Boss :** Snake

---

#### **Table `players`**
Stocke les données de tous les joueurs

| Colonne | Type | Défaut | Description |
|---------|------|--------|-------------|
| `PlayerID` | VARCHAR(40) | - | UUID unique (PRIMARY KEY) |
| `Vie` | INT | 100 | Points de vie maximum |
| `AtkDeBase` | INT | 1 | Valeur d'attaque de base |
| `ReducDegat` | INT | 0 | Réduction de dégâts reçus |
| `Argent` | INT | 0 | Argent en jeu |
| `Name` | VARCHAR(10) | - | Nom du joueur (UNIQUE) |
| `MDP` | VARCHAR(30) | - | Mot de passe (stocké en clair ⚠️) |
| `Volume` | FLOAT | 0.2 | Volume audio (0.0 à 1.0) |
| `Weapons` | VARCHAR(24) | `[[2, 0, 0], [1, 0, 0]]` | Inventaire d'armes (matrice 2x3) |

**Données de test :**
```
PlayerID: 368b4e87-fd2c-4f06-aa56-a8ee6fa9a42f
- Nom: Bernard, MDP: Patate10, Vie: 100, Argent: 0

PlayerID: 7e176586-3829-4c65-8df8-528faeb87beb
- Nom: Orneige, MDP: emojiSmegma, Vie: 100, Argent: 200
- Armes: Bannane (ID 2) et Branche (ID 1 avec 2 en slot 3)
```

---

#### **Table `weapons`**
Catalogue des armes disponibles

| Colonne | Type | Défaut | Description |
|---------|------|--------|-------------|
| `Nom` | VARCHAR(20) | - | Nom de l'arme (PRIMARY KEY) |
| `Effet` | VARCHAR(20) | NULL | Effet spécial (ex: "Poison", "Soin") |
| `Taille` | VARCHAR(6) | '1X1' | Taille dans l'inventaire |
| `Rarete` | VARCHAR(20) | - | Rareté : Pourie, Ok, Rare, Légendaire |
| `Degats` | INT | - | Dégâts infligés |

**Armes actuellement en BD (3) :**
1. **Branche** - Rareté: Pourie, Dégâts: 10, Taille: 1x1
2. **Épée rouillée** - Rareté: Pourie, Dégâts: 17, Taille: 1x1
3. **Hache de fer** - Rareté: Ok, Dégâts: 32, Taille: 1x2

**Note :** Le code implémente 6 armes (Branche, Banane, Hache de Fer, Épée Rouillée, Lance, Toile), mais seules 3 sont en base

---

### **Relation entre fichiers et DB**

```
CheckDB.py (Initialisation)
    ↓
testosterone.sql (Schéma)
    ↓
PlayerStats.py (Accès Joueur)
├─ GetLife(), GetAtk(), GetReducDegat()
├─ AddLife(), AddArgent()
└─ OG(), SignIn()

WeaponsStats.py (Accès Armes)
├─ GetWeapons()
├─ GetPourrieWeapons()
├─ GetOkWeapons()
└─ GetLegendaireWeapons()

EnnemiesStats.py (Accès Ennemis)
├─ GetDamageDealers()
├─ GetTanks()
├─ GetSupports()
└─ GetBoss()
```

---

### **Points Importants**

✅ **Problèmes identifiés :**
1. **Sécurité :** Mots de passe stockés en clair ❌
2. **Incohérence d'armes :** Seules 3 armes en BD vs 6 implémentées dans le code
3. **Inventaire :** Format de texte (`VARCHAR`) au lieu de table relationnelle
4. **Atout d'ennemi :** Non utilisé dans le code actuel

✅ **Points forts :**
- Structure claire avec clés primaires et uniques
- Charset UTF-8 pour caractères spéciaux
- Données de test présentes
- Script exportable pour sauvegarde/partage

**État global DB :** ✅ Fonctionnel mais nécessite une migration aux armes manquantes

---

## 🏗️ Structure Générale

### **Architecture du Jeu**

```
┌─────────────────────────────┐
│    Main.py (Titre)          │
│    ↓ "Play" button          │
├─────────────────────────────┤
│    Spawn.py (Hub)           │
│    ├─ Shop → ShopView.py    │
│    └─ Portal → Map/MapBoss  │
├─────────────────────────────┤
│    Map.py (Progression)     │
│    ├─ 4 positions sur map   │
│    ├─ Combat → FightScene   │
│    └─ Bonus → Bonus_lvl     │
├─────────────────────────────┤
│    FightScene.py (Combat)   │
│    ├─ jusqu'à 3 ennemis     │
│    ├─ Système de tours      │
│    ├─ Récompense StatueView │
│    └─ Mort → Spawn          │
├─────────────────────────────┤
│    BossFight.py (Boss)      │
│    ├─ 1 ennemi unique       │
│    ├─ Même système de combat│
│    └─ Progression ++        │
└─────────────────────────────┘
```

### **Flux de Données**

**BASE DE DONNÉES (MySQL - "testosterone")**
```
Players Table                Weapons Table           Enemies Table
├─ PlayerID (UUID)          ├─ ID                   ├─ Nom
├─ Name                     ├─ Nom                  ├─ Type (Tank/DamageDealer/Support/Boss)
├─ MDP                      ├─ Rarete               ├─ PV
├─ Vie                      └─ Dégâts               └─ Attaque
├─ Attaque
├─ ReducDegat
├─ Argent
└─ Items (inventaire)
```

---

## 🎯 Système de Difficulté

La difficulté progresse avec le compteur de cartes (`compteur_maps`):
- **Compteur < 6** : 1 ennemi, difficulté faible
- **Compteur 6-10** : 2 ennemis, difficulté moyenne
- **Compteur > 10** : 3 ennemis, difficulté élevée
- **Cartes multiples de 10** : Combat de boss

---

## 🎨 Ressources Multimédia Utilisées

### **Images :**
- perso.png, TITLE.png, SHOP.png, portal.png, gear.png
- herbe.webp, pathcomplet.png, stonepath.png, Target.png
- Ennemis : banana.png, spider.png, gorilla.png, ouaso.png, groazo.png, ours.png
- Items : potionverte.png, epeeblack.png, coins.png, statue.png, bonus_floor.jpg, church.webp
- Icônes : start.png, battle.png, area.png, end.png, bossmort.png

### **Sons :**
- pas.wav, Scream.wav, musicfight.mp3

---

## ⚡ État Global du Projet

| Catégorie | État | Notes |
|-----------|------|-------|
| **Base de Données** | ✅ | CheckDB.py fonctionne; 3 armes en BD vs 6 implémentées |
| **Schéma BD** | ✅ | Tables bien structurées, données de test présentes |
| **Gestion BD** | ✅ | PlayerStats, Weapons, Enemies Stats |
| **Joueur** | ✅ | Classe player fonctionnelle |
| **Ennemis** | ✅ | Génération aléatoire, 3 types + Boss |
| **Combat basique** | ✅ | FightScene fonctionnelle |
| **Combat Boss** | ✅ | BossFight fonctionnelle |
| **Armes** | ✅ | 6 armes implémentées |
| **Animations** | ✅ | Basiques (phase 1 seulement complètement implémentée) |
| **Map/Navigation** | ✅ | Map et MapBoss fonctionnelles |
| **Boutique** | ✅ | Basique, WeaponShop non implémentée |
| **Menu** | ✅ | Options non complètement développées |
| **Hub/Spawn** | ✅ | Fonctionnel avec collisions |

---

## 📝 Notes de Développement

1. **Points forts :**
   - Architecture bien organisée avec séparation données/logique/UI
   - Système de difficultés adaptatif
   - Gestion cohérente des ressources multimédia

2. **Points à améliorer :**
   - Compléter les animations (phases 2, 3, etc.)
   - Implémenter `WeaponShop` complet
   - Améliorer l'affichage du menu Options
   - Ajouter plus de variété aux armes/ennemis

3. **Dépendances :**
   - Arcade (GUI, sprites, sons)
   - mysql.connector (base de données)
   - uuid (construction des identifiants)

---
