from typing import List

from src.models.score_model import ScoreModel


class RollModel:

    def __init__(self, turn, rolls: [int], score: int, dice_sorted: int, dice_result_sorted: List[ScoreModel]):
        self.turn = turn
        self.ROLLS: [int] = rolls
        self.SCORE: int = score
        self.DICE_SORTED: int = dice_sorted
        self.DICE_RESULT_SORTED: List[ScoreModel] = dice_result_sorted
