import random


class DiceModel:
    # Nombre de faces des dés
    NB_DICE_FACES = 6

    def get_rolls_dice(self, nb_dice_to_roll):
        """Launch the dice and set a list with an occurrence of each value return by the dice
        Parameters
        ----------
        nb_dice_to_roll : int
            the number of dice with have to roll
        Returns
        -------
        list
            a list with all the occurrence for each side dice
        """
        dice_value_occurrence_list = [0] * self.NB_DICE_FACES
        for index in range(nb_dice_to_roll):
            dice_value = random.randint(1, self.NB_DICE_FACES)
            dice_value_occurrence_list[dice_value - 1] += 1
        return dice_value_occurrence_list