from methods.models.turn_model import TurnModel


class PlayerModel:
    score = 0

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
        turn_method = TurnModel(self, new_turn_value)
        self.TURN_LIST.append(turn_method)

    def get_player_total_lost_score(self):
        total_lost_score = 0
        total_turns = 0
        for turn in self.TURN_LIST:
            if turn.TURN_LOOSE:
                score_lost_turn = turn.get_potential_lost_points()
                total_lost_score += score_lost_turn
                total_turns += 1
        return total_lost_score, total_turns

    def get_player_total_score(self):
        self.score = 0
        total_turns = 0
        for turn in self.TURN_LIST:
            if not turn.TURN_LOOSE:
                score_turn = turn.get_turn_score()
                self.score += score_turn
                total_turns += 1

        if self.score >= self.game_model.DEFAULT_TARGET_SCORE:
            self.winner = True

        return self.score, total_turns

    def get_player_turns(self):
        return len(self.TURN_LIST)

    def get_player_results(self):
        total_score, total_turns = self.get_player_total_score()
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

    def get_max_turn_score(self):
        player_max_turn_score = 0
        for turn in self.TURN_LIST:
            turn_score = turn.get_turn_score()
            if turn_score >= player_max_turn_score:
                player_max_turn_score = turn_score
        return player_max_turn_score

    def get_longest_turn(self):
        player_longest_turn = 0
        for turn in self.TURN_LIST:
            rolls_length = turn.get_rolls_length()
            if rolls_length >= player_longest_turn:
                player_longest_turn = rolls_length
        return player_longest_turn

    def get_max_potential_lost_points(self):
        potential_lost_points_max = 0
        for turn in self.TURN_LIST:
            potential_lost_points = turn.get_potential_lost_points()
            if potential_lost_points >= potential_lost_points_max:
                potential_lost_points_max = potential_lost_points
        return potential_lost_points_max
