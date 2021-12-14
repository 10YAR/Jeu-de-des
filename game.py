from models.player_model import PlayerModel
from settings.game_setting import GameSetting


def main():
    game = GameSetting()

    player_1 = PlayerModel('Jean')
    player_2 = PlayerModel('Romain')

    game.add_players(player_1, player_2)


main()
