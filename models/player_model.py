class PlayerModel:
    # Scores du joueur
    score = 0

    # Dés restants des joueurs
    remaining_dice = 0

    # Tours joués de chaque joueurs
    total_rolls = 0

    # Bonus gagnés de chaque joueurs
    total_bonus = 0

    # Pertes de points de chaque joueurs
    total_potential_loss = 0

    winner = False

    def __init__(self, name):
        self.name = name
