# 🏰 A-MAZE-ING

## Description

Un générateur de labyrinthes interactif en Python utilisant l'algorithme Growing Tree. Le programme génère des labyrinthes parfaits ou imparfaits et permet de visualiser le chemin de l'entrée à la sortie.

---

## 📋 Table des matières

- [Fonctionnalités](##fonctionnalités)
- [Installation](##installation)
- [Utilisation](##utilisation)
- [Configuration](##configuration)
- [Architecture](##architecture)
- [Algorithmes](#algorithmes)
- [Auteurs](#auteurs)

---

## ✨ Fonctionnalités

- ✅ Génération aléatoire de labyrinthes
- ✅ Algorithme Growing Tree pour labyrinthes parfaits
- ✅ Support des labyrinthes imparfaits (défectueux)
- ✅ Affichage interactif du labyrinthe
- ✅ Visualisation du chemin de l'entrée à la sortie
- ✅ Système de couleurs personnalisable
- ✅ Gestion des configurations via fichier `config.txt`

**À COMPLÉTER** : Ajoutez d'autres fonctionnalités si elles existent.

---

## 🚀 Installation

### Prérequis

```bash
- Python 3.10+
- pip ou venv
```

### Étapes

1. **Cloner le repository**
   ```bash
   git clone <URL_DU_REPO>
   cd A-MAZE-ING
   ```

2. **Créer un environnement virtuel**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirement.txt
   ```

**À COMPLÉTER** : Ajoutez des instructions spécifiques si nécessaire.

---

## 💻 Utilisation

### Lancement du programme

```bash
make run
```

ou directement :

```bash
python3 a_maze_ing.py config.txt
```

### Menu interactif

Lors du lancement, vous verrez le menu suivant :

```
1 - Re-generate a new maze
2 - Show/Hide path from entry to exit
3 - Rotate maze colors
4 - Quit
```

**À COMPLÉTER** : Détaillez chaque option du menu.

---

## ⚙️ Configuration

Le fichier `config.txt` permet de personnaliser les paramètres du labyrinthe :

```ini
WIDTH=20              # Largeur du labyrinthe
HEIGHT=20             # Hauteur du labyrinthe
ENTRY=2,6             # Point d'entrée (x,y)
EXIT=6,8              # Point de sortie (x,y)
OUTPUT_FILE=maze.txt  # Fichier de sortie
PERFECT=True          # Labyrinthe parfait (True/False)
SEED=                 # Graine aléatoire (optionnel)
```

**À COMPLÉTER** : Expliquez les impacts de chaque paramètre.

---

## 📁 Architecture

```
A-MAZE-ING/
├── maze_algorithm/
│   ├── __init__.py             # Rend le dossier importable
│   ├── maze.py                 # Classe de base MazeGenerator (à créer/renommer)
│   ├── growing_tree.py         # Algorithme Growing Tree
│   └── defective_maze.py       # Génération de labyrinthes imparfaits
├── tools1/
│   ├── __init__.py             # Rend le dossier importable
│   ├── bfs_algorithm.py        # Algorithme BFS pour trouver le chemin
│   └── gen_output.py           # Génération de fichiers de sortie
├── visualize/
│   ├── __init__.py             # Rend le dossier importable
│   ├── draw.py                 # Affichage ASCII du labyrinthe
│   ├── parsing.py              # Parsing des configurations
│   └── utils.py                # Utilitaires
├── .gitignore                  # Exclusion des fichiers inutiles (__pycache__, .whl)
├── a_maze_ing.py               # Fichier principal (Point d'entrée)
├── config.txt                  # Fichier de configuration par défaut
├── Makefile                    # Automatisation (build, clean, test)
├── maze.txt                    # Fichier de sortie (généré par le programme)
├── pyproject.toml              # Configuration du packaging et des dépendances
├── README.md                   # Documentation du projet
└── requirement.txt             # Liste des bibliothèques Python
```

---

## 🧮 Algorithmes

### Growing Tree (Croissance d'arbre)
<img width="3000" height="2000" alt="1036 8" src="https://github.com/user-attachments/assets/160e18a4-819a-4801-b2f9-5ef0eb3fabe1" />

Regarder l'algorithme: https://weblog.jamisbuck.org/2011/1/27/maze-generation-growing-tree-algorithm

Explication de l'algorithme Growing Tree en détail:

1. Partir d'une cellule de départ...
2. Choisis des directions aléatoires
3. Dans le cas où aucune direction n'est possible, cul de sac
4. L'algorithme revient sur ses pas jusqu'à retrouver une direction
5. L'algorithme s'arrête quand le chemin revient à sa position initiale

---

### Recherche du chemin (BFS)

Explication de l'algorithme BFS (Breadth-First Search) en détail:

1. **Initialisation** : Placer la cellule de départ dans une file d'attente (queue) et marquer cette cellule comme visitée.
2. **Exploration niveau par niveau** : Tant que la file n'est pas vide :
   - Retirer la cellule en tête de file (cellule actuelle).
   - Si cette cellule est la sortie, reconstruire le chemin en remontant les parents.
   - Sinon, explorer les quatre voisins possibles (haut, droite, bas, gauche) si ils sont valides (dans les limites du labyrinthe et sans mur).
   - Pour chaque voisin non visité, le marquer comme visité, l'ajouter à la file, et enregistrer la cellule actuelle comme parent avec la direction.
3. **Fin** : Si la file se vide sans avoir atteint la sortie, aucun chemin n'existe. Sinon, le chemin est reconstruit en utilisant les données de parent stockées.

---

## 🧪 Commandes utiles

### Développement

```bash
make lint          # Vérifier le code avec flake8 et mypy
make debug         # Lancer en mode débogage
make clean         # Nettoyer les fichiers __pycache__
make install       # Installer les dépendances
```

## 📊 Format de sortie

Le fichier de sortie `maze.txt` contient: l'hexadécimal du labyrinthe avec l'entrée, la sortie et le chemin de résolution du labyrinthe
```
d5513913953951555553
9552eaaac3c6ba95553e
ad5696ac3c392ac553c3
83956969696eac513c3a
aac396ba96914396e96a
ac52ab86abaad2a956ba
abbeac47ac2c3ec6916a
aac3c553c3c7c1552a96
c43c53f83afff857aec3
93c17afec057fa95293a
ae9696fffafffac3eac2
a947ad13fafd507c3c3e
8695696afafffe952bc3
a96d543c3ad1516d4292
ac5539696c5696953aae
8579683c553d47abaec3
a93abaa953c3956ac53a
aac6c6ac7a96853853c2
aa93956956c3c7a83c7a
ec6c6d545554556ec556

2,6
19,19
SESEESSWSSWWSWSEEESWSSWNWSSSENESENEENNNWNENWNENESS....
```
---

## 👥 Auteurs

- Fleur Caval
- Benjamin Beaurain
