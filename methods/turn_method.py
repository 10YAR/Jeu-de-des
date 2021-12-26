import random

from methods.roll_method import RollMethod


class TurnMethod:
    TURN = None
    TURN_DONE = False
    TURN_LOOSE = False

    ROLL = 1

    NB_DICE_ROLLS = 0

    def __init__(self, player, turn):
        self.player = player
        self.TURN = turn
        self.NB_DICE_ROLLS = player.game_model.NB_DICE_ROLLS
        self.ROLL_LIST = []

    def set_roll_done(self, rolls, score, dice_sorted, dice_result_sorted):
        self.NB_DICE_ROLLS -= dice_sorted

        roll_method = RollMethod(self, rolls, score, dice_sorted, dice_result_sorted)
        self.ROLL_LIST.append(roll_method)
        self.ROLL_LIST = self.ROLL_LIST[:]
        return self.ROLL_LIST[-1]

    def set_turn_done(self):
        self.TURN_DONE = True

    def get_last_roll(self):
        return self.ROLL_LIST[-1]

    def add_roll(self):
        self.ROLL += 1
        return self.ROLL

    def get_turn_score(self):
        score_turn = 0
        for roll_selected in self.ROLL_LIST:
            score_turn += roll_selected.SCORE
        return score_turn

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
            f"turn score {score_turn}, remaining dice to roll : {self.NB_DICE_ROLLS}"
        )

    def get_turn_next_roll_logic(self):
        last_roll = self.get_last_roll()
        score_turn, dice_turn_sorted = self.get_turn_score_and_dice_left()

        if last_roll.SCORE <= 0:
            print(f"You lose this turn and a potential to score {score_turn} pts.")
            self.TURN_LOOSE = True
            self.set_turn_done()
        else:
            if not self.TURN_DONE and not self.TURN_LOOSE and self.NB_DICE_ROLLS > 0:
                if self.get_next_player_roll_response():
                    self.add_roll()
                else:
                    self.set_turn_done()
                    print(f"You win this turn, scoring {score_turn} pts")

            else:
                print(f"You win this turn, scoring {score_turn} pts")

    def get_next_player_roll_response(self):
        if not self.player.game_model.DEBUG:
            input_continue = input("Continue ? y/n (yes)")
        else:
            input_continue = random.choice(['yes', 'n'])
        return input_continue != 'n'
