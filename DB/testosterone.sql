-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 12 jan. 2026 à 08:50
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `testosterone`
--

-- --------------------------------------------------------

--
-- Structure de la table `enemies`
--

CREATE TABLE `enemies` (
  `Nom` varchar(20) NOT NULL,
  `Type` varchar(20) NOT NULL,
  `Atout` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `enemies`
--

INSERT INTO `enemies` (`Nom`, `Type`, `Atout`) VALUES
('Araignee', 'Support', 'Poison'),
('Gorille', 'Tank', NULL),
('Singe', 'DamageDealer', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `players`
--

CREATE TABLE `players` (
  `PlayerID` varchar(40) NOT NULL,
  `Vie` int(11) NOT NULL DEFAULT 100,
  `AtkDeBase` int(11) NOT NULL DEFAULT 1,
  `ReducDegat` int(11) NOT NULL DEFAULT 0,
  `Argent` int(11) NOT NULL DEFAULT 0,
  `Name` varchar(10) NOT NULL,
  `MDP` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `players`
--

INSERT INTO `players` (`PlayerID`, `Vie`, `AtkDeBase`, `ReducDegat`, `Argent`, `Name`, `MDP`) VALUES
('368b4e87-fd2c-4f06-aa56-a8ee6fa9a42f', 100, 1, 0, 0, 'Bernard', 'Patate10'),
('7e176586-3829-4c65-8df8-528faeb87beb', 100, 1, 0, 0, 'Orneige', 'emojiSmegma');

-- --------------------------------------------------------

--
-- Structure de la table `weapons`
--

CREATE TABLE `weapons` (
  `Nom` varchar(20) NOT NULL,
  `Effet` varchar(20) DEFAULT NULL,
  `Taille` varchar(6) NOT NULL DEFAULT '1X1',
  `Rarete` varchar(20) NOT NULL,
  `Degats` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `weapons`
--

INSERT INTO `weapons` (`Nom`, `Effet`, `Taille`, `Rarete`, `Degats`) VALUES
('Branche', NULL, '1X1', 'Pourie', 10),
('Épée rouillée', NULL, '1X1', 'Pourie', 17),
('Hache de fer', NULL, '1X2', 'Ok', 32);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `enemies`
--
ALTER TABLE `enemies`
  ADD PRIMARY KEY (`Nom`);

--
-- Index pour la table `players`
--
ALTER TABLE `players`
  ADD PRIMARY KEY (`PlayerID`),
  ADD UNIQUE KEY `Name` (`Name`);

--
-- Index pour la table `weapons`
--
ALTER TABLE `weapons`
  ADD PRIMARY KEY (`Nom`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
