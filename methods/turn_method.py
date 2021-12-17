from methods.roll_method import RollMethod


class TurnMethod:
    TURN = None
    TURN_DONE = False

    ROLL = 0
    ROLL_LIST = []

    def __init__(self, turn, nb_dice_rolls):
        self.TURN = turn
        self.NB_DICE_ROLLS = nb_dice_rolls

    def set_roll_done(self, rolls, score):
        roll_method = RollMethod(rolls, score)

        self.ROLL_LIST.append(roll_method)
        self.ROLL_LIST = self.ROLL_LIST[:]
        return self.ROLL_LIST[-1]

    def add_roll(self):
        self.ROLL += 1
        return self.ROLL
