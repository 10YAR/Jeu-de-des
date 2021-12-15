class ScoreSetting:
    # Score à atteindre
    DEFAULT_TARGET_SCORE = 2000

    # Nombre d'occurences pour déclencher le bonus
    TRIGGER_OCCURRENCE_FOR_BONUS = 3

    # Multiplicateur de points pour un bonus classique
    BONUS_VALUE_FOR_NORMAL_BONUS = 100

    # Multiplicateur de points pour un ACE
    BONUS_VALUE_FOR_ACE_BONUS = 1000

    def __init__(self, winner_figure_value, winner_figure_multiplier):
        self.winner_figure_value = winner_figure_value
        self.winner_figure_multiplier = winner_figure_multiplier


