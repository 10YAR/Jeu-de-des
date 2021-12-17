from methods.roll_method import RollMethod


class TurnMethod:
    TURN = None
    TURN_DONE = False

    ROLL = 0
    ROLL_LIST = []

    def __init__(self, turn, nb_dice_rolls):
        self.TURN = turn
        self.NB_DICE_ROLLS = nb_dice_rolls

    def set_roll_done(self, rolls, score, dice_sorted, dice_result_sorted):
        roll_method = RollMethod(rolls, score, dice_sorted, dice_result_sorted)
        self.ROLL_LIST.append(roll_method)
        self.ROLL_LIST = self.ROLL_LIST[:]
        return self.ROLL_LIST[-1]

    def get_last_roll(self):
        return self.ROLL_LIST[-1]

    def add_roll(self):
        self.ROLL += 1
        return self.ROLL

    def get_turn_score_and_dice_left(self):
        score_turn = 0
        dice_turn_sorted = 0

        for roll_selected in self.ROLL_LIST:
            score_turn += roll_selected.SCORE
            dice_turn_sorted += roll_selected.DICE_SORTED

        return score_turn, dice_turn_sorted

    @staticmethod
    def get_display_roll_scoring_dice(roll_selected):
        display = ''
        for idx, dice_result in enumerate(roll_selected.DICE_RESULT_SORTED):
            display += f"({dice_result.WINNER_FIGURE_VALUE}, {dice_result.DICE_NUMBER})"
            if idx < (len(roll_selected.DICE_RESULT_SORTED) - 1):
                display += ', '
        return display

    def get_roll_result(self):
        last_roll = self.get_last_roll()
        score_turn, dice_turn_sorted = self.get_turn_score_and_dice_left()
        
        print(
            f"roll #{self.ROLL}: {last_roll.DICE_SORTED} scoring dices [{self.get_display_roll_scoring_dice(last_roll)}] scoring {last_roll.SCORE}, potential total "
            f"turn score {score_turn}, remaining dice to roll : {self.NB_DICE_ROLLS - dice_turn_sorted}"
        )
