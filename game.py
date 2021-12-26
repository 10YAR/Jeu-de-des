from models.dice_model import DiceModel
from models.game_model import GameModel
from models.player_model import PlayerModel
from settings.score_bonus_setting import ScoreBonusSetting


def main():
    game = GameModel()
    dice_model = DiceModel()

    player_1 = PlayerModel('Jean')
    player_2 = PlayerModel('Romain')

    game.add_players(player_1, player_2)

    score_bonus_1 = ScoreBonusSetting(1, 100)
    score_bonus_2 = ScoreBonusSetting(5, 50)

    game.add_scores(score_bonus_1, score_bonus_2)

    while not game.get_player_winner():
        player_turn, turn_selected = game.get_player_turn()

        if turn_selected.ROLL == 1:
            print(f"Turn #{game.TURNS} --> {player_turn.name} | score: {player_turn.score}")

        rolls = dice_model.get_rolls_dice(turn_selected.NB_DICE_ROLLS)

        score, dice_sorted, dice_result_sorted = game.calculate_score(dice_model.NB_DICE_FACES, rolls)

        turn_selected.set_roll_done(rolls, score, dice_sorted, dice_result_sorted)
        turn_selected.get_roll_result()
        turn_selected.get_turn_next_roll_logic()

        game.get_players_dashboard(turn_selected)

    print(game.get_player_winner())


main()
