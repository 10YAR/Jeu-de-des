from models.dice_model import DiceModel
from models.player_model import PlayerModel
from models.score_model import ScoreModel
from settings.game_setting import GameSetting


def main():
    game = GameSetting()

    player_1 = PlayerModel('Jean')
    player_2 = PlayerModel('Romain')

    game.add_players(player_1, player_2)

    dice_model = DiceModel()

    while not game.get_player_winner():
        player_turn = game.get_player_turn()
        print(f"Turn #{game.TURNS} --> {player_turn.name} | score: {player_turn.score}")

        player_1.winner = True


main()
