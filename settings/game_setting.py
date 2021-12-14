# Score à atteindre
DEFAULT_TARGET_SCORE = 2000
# Nombre de faces des dés
NB_DICE_FACES = 6
# Nombre de dés jetés
NB_DICE_ROLLS = 3
# Chiffres gagnants du dés
LIST_SCORING_DICE_VALUE = [1, 5]
# Points associés aux chiffres gagnants du dés
LIST_SCORING_MULTIPLIER = [100, 50]
# Nombre d'occurences pour déclencher le bonus
TRIGGER_OCCURRENCE_FOR_BONUS = 3
# Multiplicateur de points pour un bonus classique
BONUS_VALUE_FOR_NORMAL_BONUS = 100
# Multiplicateur de points pour un ACE
BONUS_VALUE_FOR_ACE_BONUS = 1000
# Liste des joueurs
PLAYERS = ["Romain", "François", "Stéphane", "Laurent", "Christophe", "Isabelle", "Sylvie"]
# Scores des joueurs
SCORES = [0] * len(PLAYERS)
# Dés restants des joueurs
REMAINING = [NB_DICE_ROLLS] * len(PLAYERS)
# Tours joués de chaque joueurs
TOTAL_ROLLS = [0] * len(PLAYERS)
# Bonus gagnés de chaque joueurs
TOTAL_BONUS = [0] * len(PLAYERS)
# Pertes de points de chaque joueurs
TOTAL_POTENTIAL_LOSS = [0] * len(PLAYERS)
# Booléen gagnant
WINNER = False
# Nombre de tours réalisés
TURNS = 0
# Score maximum réalisé dans un tour par un joueur
MAX_TURN_SCORING = ["", 0]
# Liste des lancés scorants
SCORING_TURNS = []
# Liste des lancés non scorants
NON_SCORING_TURNS = []

# Debug
DEBUG = True