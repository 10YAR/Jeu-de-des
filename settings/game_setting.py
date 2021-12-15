class GameSetting:
    # Score à atteindre

    DEFAULT_TARGET_SCORE = 2000

    # Nombre de dés a jeter
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
    PLAYERS = []

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

    PLAYER_TURN = None

    def add_turn(self):
        self.TURNS += 1
        return self.TURNS

    def get_player_length(self):
        return len(self.PLAYERS)

    def add_players(self, *players):
        """The function adds players to the game.

            Parameters
            ----------
            players : PlayerModel
                Player model entity
        """
        self.PLAYERS = players

        if self.get_player_length() > 0:
            self.PLAYER_TURN = self.PLAYERS[0]

    def get_player_winner(self):
        """The function checks if a player wins the game.

            Returns
            -------
            PlayerModel
            The game winner
            -------
            Boolean<false>
        """
        for player in self.PLAYERS:
            if player.winner:
                return player
        return False

    def get_player_turn(self):

        self.PLAYER_TURN.remaining_dice = self.NB_DICE_ROLLS

        return self.PLAYER_TURN
