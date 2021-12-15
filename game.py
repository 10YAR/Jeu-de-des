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

    # for player in game.PLAYERS_LIST:
    #     turn_last = player.TURN_LIST[-1]
    #     print(player.name, turn_last.TURN, turn_last.TURN_DONE, turn_last)

    while not game.get_player_winner():
        player_turn, turn_selected = game.get_player_turn()

        if turn_selected.ROLL == 0:
            print(f"Turn #{game.TURNS} --> {player_turn.name} | score: {player_turn.score}")







        if turn_selected.ROLL > 5:
            print('okkkkkkkkkkkkkkkkk')
            player_turn.set_last_turn_done()

        turn_selected.add_roll()

        if game.TURNS == 3:
            player_1.winner = True


main()
