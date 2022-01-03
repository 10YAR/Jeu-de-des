class GameSetting:
    # Nombre de dés a jeter
    NB_DICE_ROLLS: int = 5

    # Nombre de tours réalisés
    TURNS: int = 0

    # Debug
    DEBUG: bool = True

    # Score à atteindre
    DEFAULT_TARGET_SCORE: int = 2000

    # Nombre d'occurences pour déclencher le bonus
    TRIGGER_OCCURRENCE_FOR_BONUS: int = 3

    # Multiplicateur de points pour un bonus classique
    BONUS_VALUE_FOR_NORMAL_BONUS: int = 100

    # Multiplicateur de points pour un ACE
    BONUS_VALUE_FOR_ACE_BONUS: int = 1000