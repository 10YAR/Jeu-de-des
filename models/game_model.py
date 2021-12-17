from settings.game_setting import GameSetting


class GameModel(GameSetting):
    # Players list
    PLAYERS_LIST = []

    #  Scores list
    SCORES_LIST = []

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
        self.PLAYERS_LIST = players
        self.set_new_turn()

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

            if not turn_last.TURN_DONE and turn_last.TURN == self.TURNS:
                return player, turn_last

        self.set_new_turn()
        return self.PLAYERS_LIST[0], self.PLAYERS_LIST[0].TURN_LIST[-1]

    def set_new_turn(self):
        new_turn_value = self.add_turn()
        for player in self.PLAYERS_LIST:
            player.add_turn_self_player(new_turn_value)

    def calculate_score(self, dice_face, rolls):
        score = 0
        dice_sorted = 0

        for face in range(dice_face):
            for score_bonus in self.SCORES_LIST:
                if face == (score_bonus.WINNER_FIGURE_VALUE - 1):
                    # print(f"rolls: {rolls[face]}, WINNER_FIGURE_VALUE: {score_bonus.WINNER_FIGURE_VALUE},face: {face}, figure mult: {score_bonus.WINNER_FIGURE_MULTIPLIER}")

                    if rolls[face] >= self.TRIGGER_OCCURRENCE_FOR_BONUS:
                        score += self.BONUS_VALUE_FOR_ACE_BONUS
                    else:
                        score += (score_bonus.WINNER_FIGURE_MULTIPLIER * rolls[face])

                    dice_sorted += rolls[face]

        return score, dice_sorted
