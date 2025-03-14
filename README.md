# Projet PLDAC : DQN et mémoire

## Description

Ce projet explore l'utilisation de Deep Q-Networks (DQN) pour prédire la prochaine action à prendre dans un environnement partiellement observable. L'objectif principal est d'implémenter un agent capable de maintenir une mémoire des actions passées afin de mieux prédire les actions futures, même en l'absence d'une observation complète de l'état actuel. Cette approche vise à améliorer la prise de décision dans des environnements où toutes les informations nécessaires ne sont pas immédiatement accessibles.

Ce projet est réalisé dans le cadre de l'UE de Projet du Master 1 DAC sous la supervision d'Olivier Sigaud.

## Structure du projet

| Dossier            | Description                                 |
|--------------------|---------------------------------------------|
| /src               | Code source principal                       |
| ├── /agents        | Implémentation des agents DQN et DDPG       |
| ├── /envs          | Environnements d'expérimentation            |
| └── /utils         | Fonctions utilitaires                       |
| /docs              | Documentation du projet                     |
| ├── /cr            | Comptes rendus hebdomadaire                 |
| └── /notebooks     | Notebooks liés au projet                    |
| /results           | Résultats et logs des expériences           |
| README.md          | Présentation du projet                      |
| .gitignore         | Fichiers à ignorer par Git                  |
| requirements.txt   | Dépendances Python                          |


## Technologies utilisées

- Python  
- BBRL
- Gymnasium  
- NumPy  
- Matplotlib  

## Installation

1. Cloner le dépôt :  
```bash
git clone https://github.com/ton-repo/projet-dqn-ddpg.git
cd projet-dqn-ddpg
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Objectifs et expériences
- Implémenter un agent DQN dans un environnement partiellement observable.
- Utiliser une mémoire pour stocker et exploiter les actions passées afin de prédire les actions futures.
- Tester et analyser les performances de l'agent sur différents environnements.
- Comparer l'impact de l'intégration de la mémoire sur la prise de décision de l'agent.
