from methods.turn_method import TurnMethod
from settings.game_setting import GameSetting


class PlayerModel(GameSetting):
    # Scores du joueur
    score = 0

    # Dés restants des joueurs
    # remaining_dice = 0

    # Tours joués de chaque joueurs
    # total_rolls = 0

    # Bonus gagnés de chaque joueurs
    # total_bonus = 0

    # Pertes de points de chaque joueurs
    # total_potential_loss = 0

    winner = False

    def __init__(self, name):
        GameSetting.__init__(self)
        self.name = name
        self.TURN_LIST = []

    def set_last_turn_done(self):
        turn_last = self.TURN_LIST[-1]
        turn_last.TURN_DONE = True

    def add_turn_self_player(self, new_turn_value):
        turn_method = TurnMethod(new_turn_value, GameSetting.NB_DICE_ROLLS)
        self.TURN_LIST.append(turn_method)

    def get_player_total_score(self):
        self.score = 0

        for turn in self.TURN_LIST:
            score_turn = turn.get_turn_score()
            self.score += score_turn

        if self.score >= self.DEFAULT_TARGET_SCORE:
            self.winner = True

        return self.score
