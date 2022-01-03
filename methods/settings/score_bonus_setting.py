class ScoreBonusSetting:
    def __init__(self, winner_figure_value: int, winner_figure_multiplier: int):
        """
        :param winner_figure_value: 1 - 6
        :param winner_figure_multiplier:
        """
        self.WINNER_FIGURE_VALUE: int = winner_figure_value
        self.WINNER_FIGURE_MULTIPLIER: int = winner_figure_multiplier
