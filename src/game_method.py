from typing import Tuple, List, Union

from src.models.score_model import ScoreModel
from src.models.turn_model import TurnModel
from src.settings.game_setting import GameSetting
from src.settings.score_bonus_setting import ScoreBonusSetting


class GameMethod(GameSetting):

    def __init__(self):
        GameSetting.__init__(self)
        self.PLAYERS_LIST: [PlayerModel] = []
        self.SCORES_LIST: [ScoreBonusSetting] = []

    def add_turn(self) -> int:
        self.TURNS += 1
        return self.TURNS

    def get_player_length(self) -> int:
        return len(self.PLAYERS_LIST)

    def get_players_dashboard(self, turn_selected) -> None:
        total_scores_dashboard: str = "Total scores: "
        for player in self.PLAYERS_LIST:
            total_score, total_turns = player.get_player_total_score()
            total_scores_dashboard += f"{player.name} --> {total_score} "

        if turn_selected.TURN_DONE or self.get_player_winner():
            print("\n", total_scores_dashboard, "\n")

    def add_players(self, *players):
        """The function adds players to the game.

            Parameters
            ----------
            players : PlayerModel
                Player model entity
        """
        for player in players:
            player.add_game_model(self)
        self.PLAYERS_LIST: [PlayerModel] = players
        self.set_new_turn()

    def add_scores(self, *scores: [ScoreBonusSetting]) -> None:
        self.SCORES_LIST: [ScoreBonusSetting] = scores

    def get_player_winner(self) -> Union[bool or PlayerModel]:
        """The function checks if a player wins the game.

            Returns
            -------
            PlayerModel
            The game winner
            -------
            Boolean<false>
        """
        for player in self.PLAYERS_LIST:
            if player.winner:
                return player
        return False

    def get_player_turn(self) -> Tuple[None, TurnModel]:
        for player in self.PLAYERS_LIST:
            turn_last: TurnModel = player.TURN_LIST[-1]

            if not turn_last.TURN_DONE and turn_last.TURN == self.TURNS:
                return player, turn_last

        self.set_new_turn()
        return self.PLAYERS_LIST[0], self.PLAYERS_LIST[0].TURN_LIST[-1]

    def set_new_turn(self) -> None:
        new_turn_value: int = self.add_turn()
        for player in self.PLAYERS_LIST:
            player.add_turn_self_player(new_turn_value)

    def calculate_score(self, dice_face: int, rolls: [int]) -> Tuple[int, int, List[ScoreModel]]:
        score: int = 0
        dice_sorted: int = 0
        dice_result_sorted: [int] = []

        for face in range(dice_face):
            for score_bonus in self.SCORES_LIST:
                if face == (score_bonus.WINNER_FIGURE_VALUE - 1):
                    if rolls[face] >= self.TRIGGER_OCCURRENCE_FOR_BONUS:
                        score += self.BONUS_VALUE_FOR_ACE_BONUS
                    else:
                        score += (score_bonus.WINNER_FIGURE_MULTIPLIER * rolls[face])

                    dice_sorted += rolls[face]

        for score_bonus in self.SCORES_LIST:
            rolls_selected: [int] = score_bonus.WINNER_FIGURE_VALUE - 1
            if rolls[rolls_selected] > 0:
                score_model: ScoreModel = ScoreModel(score_bonus.WINNER_FIGURE_VALUE, rolls[rolls_selected])
                dice_result_sorted.append(score_model)

        return score, dice_sorted, dice_result_sorted

    def get_results_dashboard(self) -> None:
        player_winner: PlayerModel = self.get_player_winner()
        print(f"Game in {player_winner.get_player_turns()} turns")
        for player in self.PLAYERS_LIST:
            player.get_player_results()

    def get_game_resume(self) -> None:
        max_turn_score: dict = {
            'player': None,
            'score': 0
        }
        longest_turn: dict = {
            'player': None,
            'length': 0
        }
        max_turn_loss: dict = {
            'player': None,
            'points': 0
        }

        total_score_global, total_turns_global = 0, 0
        total_score_lost_global, total_turns_lost_global = 0, 0

        for player in self.PLAYERS_LIST:
            player_max_turn_score: int = player.get_max_turn_score()
            if player_max_turn_score >= max_turn_score['score']:
                max_turn_score = {
                    'player': player,
                    'score': player_max_turn_score
                }

            player_longest_turn: int = player.get_longest_turn()
            if player_longest_turn >= longest_turn['length']:
                longest_turn = {
                    'player': player,
                    'length': player_longest_turn
                }

            player_max_potential_lost_points: int = player.get_max_potential_lost_points()
            if player_max_potential_lost_points >= max_turn_loss['points']:
                max_turn_loss = {
                    'player': player,
                    'points': player_max_potential_lost_points
                }

            total_score, total_turns = player.get_player_total_score()
            total_score_global += total_score
            total_turns_global += total_turns

            total_score_lost, total_turns_lost = player.get_player_total_lost_score()
            total_score_lost_global += total_score_lost
            total_turns_lost_global += total_turns_lost

        print(f"\nMax turn scoring: {max_turn_score['player'].name} with {max_turn_score['score']} points.")
        print(f"Longest turn: {longest_turn['player'].name} with {longest_turn['length']} rolls.")
        print(f"Max turn loss: {max_turn_loss['player'].name} with {max_turn_loss['points']} points.")

        print(
            f"\nMean scoring turn: {round(total_score_global / total_turns_global, 2)} points ({total_turns_global} turns)")
        print(
            f"Mean non scoring turn: {round(total_score_lost_global / total_turns_lost_global, 2)} points ({total_turns_lost_global} turns)")
