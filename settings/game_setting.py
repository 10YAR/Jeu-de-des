from methods.turn_method import TurnMethod


class GameSetting:
    # Nombre de dés a jeter
    NB_DICE_ROLLS = 5

    # Nombre de tours réalisés
    TURNS = 0

    # Debug
    DEBUG = True

    # Score à atteindre
    DEFAULT_TARGET_SCORE = 2000

    # Nombre d'occurences pour déclencher le bonus
    TRIGGER_OCCURRENCE_FOR_BONUS = 3

    # Multiplicateur de points pour un bonus classique
    BONUS_VALUE_FOR_NORMAL_BONUS = 100

    # Multiplicateur de points pour un ACE
    BONUS_VALUE_FOR_ACE_BONUS = 1000