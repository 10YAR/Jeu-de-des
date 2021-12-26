from models.score_model import ScoreModel
from settings.game_setting import GameSetting


class GameModel(GameSetting):

    def __init__(self):
        GameSetting.__init__(self)
        self.PLAYERS_LIST = []
        self.SCORES_LIST = []

    def add_turn(self):
        self.TURNS += 1
        return self.TURNS

    def get_player_length(self):
        return len(self.PLAYERS_LIST)

    def get_players_dashboard(self, turn_selected):
        total_scores_dashboard = "Total scores: "
        for player in self.PLAYERS_LIST:
            score = player.get_player_total_score()
            total_scores_dashboard += f"{player.name} --> {score} "

        if turn_selected.TURN_DONE:
            print("\n", total_scores_dashboard, "\n")

    def add_players(self, *players):
        """The function adds players to the game.

            Parameters
            ----------
            players : PlayerModel
                Player model entity
        """
        for player in players:
            player.add_game_model(self)
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
        dice_result_sorted = []

        for face in range(dice_face):
            for score_bonus in self.SCORES_LIST:
                if face == (score_bonus.WINNER_FIGURE_VALUE - 1):
                    if rolls[face] >= self.TRIGGER_OCCURRENCE_FOR_BONUS:
                        score += self.BONUS_VALUE_FOR_ACE_BONUS
                    else:
                        score += (score_bonus.WINNER_FIGURE_MULTIPLIER * rolls[face])

                    dice_sorted += rolls[face]

        for score_bonus in self.SCORES_LIST:
            rolls_selected = score_bonus.WINNER_FIGURE_VALUE - 1
            if rolls[rolls_selected] > 0:
                score_model = ScoreModel(score_bonus.WINNER_FIGURE_VALUE, rolls[rolls_selected])
                dice_result_sorted.append(score_model)
                dice_result_sorted = dice_result_sorted[:]

        return score, dice_sorted, dice_result_sorted
