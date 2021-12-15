from models.player_model import PlayerModel
from settings.game_setting import GameSetting
from settings.score_setting import ScoreSetting


def main():
    game = GameSetting()

    player_1 = PlayerModel('Jean')
    player_2 = PlayerModel('Romain')

    game.add_players(player_1, player_2)

    score_1 = ScoreSetting(1, 100)
    score_2 = ScoreSetting(5, 50)

    game.add_scores(score_1, score_2)

    while not game.get_player_winner():
        player_turn = game.get_player_turn()

        # print(player_turn.name)

        print(f"Turn #{game.TURNS} --> {player_turn.name} | score: {player_turn.score}")

        player_turn.set_last_turn_done()

        if game.TURNS == 3:
            player_1.winner = True


main()
