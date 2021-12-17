from methods.turn_method import TurnMethod
from settings.game_setting import GameSetting


class PlayerModel(GameSetting):
    # Scores du joueur
    score = 0

    # Dés restants des joueurs
    remaining_dice = 0

    # Tours joués de chaque joueurs
    total_rolls = 0

    # Bonus gagnés de chaque joueurs
    total_bonus = 0

    # Pertes de points de chaque joueurs
    total_potential_loss = 0

    winner = False

    TURN_LIST = []

    def __init__(self, name):
        GameSetting.__init__(self)
        self.name = name

    def set_last_turn_done(self):
        turn_last = self.TURN_LIST[-1]
        turn_last.TURN_DONE = True

    def add_turn_self_player(self, new_turn_value):
        turn_method = TurnMethod(new_turn_value, GameSetting.NB_DICE_ROLLS)
        self.TURN_LIST.append(turn_method)
        self.TURN_LIST = self.TURN_LIST[:]
