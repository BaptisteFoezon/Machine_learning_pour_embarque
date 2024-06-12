# Machine learning pour embarque
Détection du Balancier à l'Aide d'un Accéléromètre et d'un Gyroscope
Description

Ce projet vise à développer un modèle de machine learning capable de détecter le mouvement de balancier à l'aide de données issues d'un accéléromètre et d'un gyroscope. Le modèle est entraîné et validé en Python en utilisant la bibliothèque scikit-learn, puis embarqué sur un microcontrôleur STM32 pour une détection en temps réel.

## Fonctionnalités

Acquisition de Données : Collecte des données brutes de l'accéléromètre et du gyroscope.
Prétraitement des Données : Nettoyage, normalisation et extraction des caractéristiques des données.
Entraînement du Modèle : Utilisation de scikit-learn pour entraîner divers modèles de machine learning.
Validation du Modèle : Évaluation des performances du modèle.
Déploiement : Intégration du modèle entraîné sur un microcontrôleur STM32 pour la détection en temps réel.

## Technologies Utilisées

Python : Langage principal pour le développement, l'entraînement et la validation des modèles.
scikit-learn : Bibliothèque utilisée pour les algorithmes de machine learning.
STM32 : Microcontrôleur utilisé pour l'implémentation embarquée du modèle.
Capteurs : Accéléromètre et gyroscope pour la collecte des données de mouvement.
