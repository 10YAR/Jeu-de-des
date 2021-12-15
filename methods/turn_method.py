class TurnMethod:
    TURN = None
    TURN_DONE = False

    def __init__(self, turn, nb_dice_rolls):
        self.TURN = turn
        self.NB_DICE_ROLLS = nb_dice_rolls
