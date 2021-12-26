from methods.turn_method import TurnMethod
from settings.game_setting import GameSetting


class PlayerModel:
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

    game_model = None

    def __init__(self, name):
        self.name = name
        self.TURN_LIST = []

    def add_game_model(self, game_model):
        self.game_model = game_model

    def set_last_turn_done(self):
        turn_last = self.TURN_LIST[-1]
        turn_last.TURN_DONE = True

    def add_turn_self_player(self, new_turn_value):
        turn_method = TurnMethod(self, new_turn_value)
        self.TURN_LIST.append(turn_method)

    def get_player_total_score(self):
        self.score = 0

        for turn in self.TURN_LIST:
            if not turn.TURN_LOOSE:
                score_turn = turn.get_turn_score()
                self.score += score_turn

        if self.score >= self.game_model.DEFAULT_TARGET_SCORE:
            self.winner = True

        return self.score

    def get_player_turns(self):
        return len(self.TURN_LIST)

    def get_player_results(self):
        total_score = self.get_player_total_score()
        rolls_total = 0
        bonus_total = 0
        potential_lost_points_total = 0
        full_roll_total = 0
        for turn in self.TURN_LIST:
            rolls_total += turn.get_rolls_length()
            bonus_total += turn.get_rolls_bonus_number()
            potential_lost_points_total += turn.get_potential_lost_points()
            full_roll_total += turn.get_full_roll_number()

        print(
            f"{self.name} {'win' if self.winner else 'lose'}! "
            f"Scoring {total_score} in {rolls_total} rolls with {full_roll_total} full roll(s), "
            f"{bonus_total} bonus and {potential_lost_points_total} points lost"
        )
