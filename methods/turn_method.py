from methods.roll_method import RollMethod
# from settings.game_setting import GameSetting


class TurnMethod:
    TURN = None
    TURN_DONE = False

    ROLL = 0
    ROLL_LIST = []

    def __init__(self, turn, nb_dice_rolls):
        # GameSetting.__init__(self)

        self.TURN = turn
        self.NB_DICE_ROLLS = nb_dice_rolls

    def set_roll_done(self, rolls, score, dice_sorted):
        roll_method = RollMethod(rolls, score, dice_sorted)

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

    def get_roll_result(self):
        last_roll = self.get_last_roll()
        score_turn, dice_turn_sorted = self.get_turn_score_and_dice_left()

        # print(GameSetting.NB_DICE_ROLLS)
        print(
            f"roll #{self.ROLL}: {last_roll.DICE_SORTED} scoring dices [] scoring {last_roll.SCORE}, potential total turn score {score_turn}, remaining dice to roll : {dice_turn_sorted}")
