import random


class DiceModel:
    # Nombre de faces des dés
    NB_DICE_FACES = 6

    def get_rolls_dice(self, nb_dice_rolls):
        rolls = [0] * self.NB_DICE_FACES
        for i in range(nb_dice_rolls):
            index = random.randint(1, self.NB_DICE_FACES)
            rolls[index - 1] += 1
        return rolls
