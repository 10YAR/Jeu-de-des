from typing import Tuple, List

from methods.game_method import GameMethod
from methods.models.turn_model import TurnModel


class PlayerModel:
    score: int = 0

    winner: bool = False

    game_model: GameMethod = None

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.TURN_LIST: List[TurnModel] = []

    def add_game_model(self, game_method: GameMethod) -> None:
        self.game_model: GameMethod = game_method

    def set_last_turn_done(self) -> None:
        turn_last = self.TURN_LIST[-1]
        turn_last.TURN_DONE = True

    def add_turn_self_player(self, new_turn_value) -> None:
        turn_method = TurnModel(self, new_turn_value)
        self.TURN_LIST.append(turn_method)

    def get_player_total_lost_score(self) -> Tuple[int, int]:
        total_lost_score: int = 0
        total_turns: int = 0
        for turn in self.TURN_LIST:
            if turn.TURN_LOOSE:
                score_lost_turn = turn.get_potential_lost_points()
                total_lost_score += score_lost_turn
                total_turns += 1
        return total_lost_score, total_turns

    def get_player_total_score(self) -> Tuple[int, int]:
        self.score: int = 0
        total_turns: int = 0
        for turn in self.TURN_LIST:
            if not turn.TURN_LOOSE:
                score_turn = turn.get_turn_score()
                self.score += score_turn
                total_turns += 1

        if self.score >= self.game_model.DEFAULT_TARGET_SCORE:
            self.winner = True

        return self.score, total_turns

    def get_player_turns(self) -> int:
        return len(self.TURN_LIST)

    def get_player_results(self) -> None:
        total_score, total_turns = self.get_player_total_score()
        rolls_total: int = 0
        bonus_total: int = 0
        potential_lost_points_total: int = 0
        full_roll_total: int = 0
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

    def get_max_turn_score(self) -> int:
        player_max_turn_score: int = 0
        for turn in self.TURN_LIST:
            turn_score = turn.get_turn_score()
            if turn_score >= player_max_turn_score:
                player_max_turn_score = turn_score
        return player_max_turn_score

    def get_longest_turn(self) -> int:
        player_longest_turn: int = 0
        for turn in self.TURN_LIST:
            rolls_length = turn.get_rolls_length()
            if rolls_length >= player_longest_turn:
                player_longest_turn = rolls_length
        return player_longest_turn

    def get_max_potential_lost_points(self) -> int:
        potential_lost_points_max: int = 0
        for turn in self.TURN_LIST:
            potential_lost_points = turn.get_potential_lost_points()
            if potential_lost_points >= potential_lost_points_max:
                potential_lost_points_max = potential_lost_points
        return potential_lost_points_max
