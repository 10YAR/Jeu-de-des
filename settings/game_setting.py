from methods.turn_method import TurnMethod


class GameSetting:
    # Nombre de dés a jeter
    NB_DICE_ROLLS = 5

    # Players list
    PLAYERS_LIST = []

    #  Scores list
    SCORES_LIST = []

    # Nombre de tours réalisés
    TURNS = 1

    # Debug
    DEBUG = True

    def add_turn(self):
        self.TURNS += 1
        return self.TURNS

    def get_player_length(self):
        return len(self.PLAYERS_LIST)

    def add_players(self, *players):
        """The function adds players to the game.

            Parameters
            ----------
            players : PlayerModel
                Player model entity
        """
        for player in players:
            turn_method = TurnMethod(self.TURNS, self.NB_DICE_ROLLS)
            player.TURN_LIST.append(turn_method)

        self.PLAYERS_LIST = players

    def add_scores(self, *scores):
        self.SCORES_LIST = scores

    def get_player_winner(self):
        """The function checks if a player wins the game.

            Returns
            -------
            PlayerModel
            The game winner
            -------
            Boolean<false>
        """
        for player in self.PLAYERS_LIST:
            if player.winner:
                return player
        return False

    def get_player_turn(self):
        for player in self.PLAYERS_LIST:
            turn_last = player.TURN_LIST[-1]
            print(player.name, turn_last.TURN, turn_last.TURN_DONE, turn_last)
            print('-----')

            if not turn_last.TURN_DONE and turn_last.TURN == self.TURNS:
                return player

        self.set_new_turn()
        return self.PLAYERS_LIST[0]

    def set_new_turn(self):
        new_turn_value = self.add_turn()

        for player in self.PLAYERS_LIST:
            turn_method = TurnMethod(new_turn_value, self.NB_DICE_ROLLS)
            player.TURN_LIST.append(turn_method)
