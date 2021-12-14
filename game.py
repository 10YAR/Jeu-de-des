from models.dice_model import DiceModel
from models.player_model import PlayerModel
from settings.game_setting import GameSetting


def main():
    game = GameSetting()

    player_1 = PlayerModel('Jean')
    player_2 = PlayerModel('Romain')

    game.add_players(player_1, player_2)

    while not game.get_player_winner():
        game.add_turn()
        dice_model = DiceModel()

        for player_turn in game.PLAYERS:
            print(f"Turn #{game.TURNS} --> {player_turn.name} | score: {player_turn.score}")

            player_turn.remaining_dice = game.NB_DICE_ROLLS

            while player_turn.remaining_dice > 0:
                print(player_turn.remaining_dice)

                rolls = dice_model.get_rolls_dice(GameSetting.NB_DICE_ROLLS)

                print('====')
                print(rolls)
                print('====')





                player_turn.remaining_dice -= 1








        player_1.winner = True


main()
