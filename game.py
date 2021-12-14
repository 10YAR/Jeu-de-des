from models.player_model import PlayerModel
from settings.game_setting import GameSetting


def main():
    game = GameSetting()

    player_1 = PlayerModel('Jean')

    # game.PLAYERS.append(player_1)

    game.add_players(player_1)
    print(game.PLAYERS)
    print(type(game.PLAYERS))


main()
