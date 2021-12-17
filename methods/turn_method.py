class TurnMethod:
    TURN = None
    TURN_DONE = False

    ROLL = 0
    ROLL_LIST = []

    def __init__(self, turn, nb_dice_rolls):
        self.TURN = turn
        self.NB_DICE_ROLLS = nb_dice_rolls

    def add_roll(self):
        self.ROLL += 1
        return self.ROLL
