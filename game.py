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

                # TODO

                # print('====')
                # print(rolls)
                # print('====')

                # myRolls, myPoints, REMAINING[i], scoringDicesTotal = calculateBonus(myRolls, REMAINING[i],usedRemainings)
                # myPoints, myRolls, REMAINING[i], scoringDicesTotal2 = calculatePoints(myRolls, myPoints, REMAINING[i],usedRemainings)

                player_points_turn = 10

                # potentialScore += myPoints
                # print("Roll #" + str(rollNumber) + " : " + str(scoringDicesTotal) + " scoring dices, scoring " + str(
                #     myPoints) + " pts, potential total turn score " + str(
                #     SCORES[i] + potentialScore) + " pts, remaining dice to roll : " + str(REMAINING[i]))

                if player_turn.get_player_turns_done(player_points_turn):
                    turn_status_input = input("Continue ? y/n :")
                    if turn_status_input == 'n':
                        player_turn.remaining_dice = 0

                else:
                    print(f"=> You lose this turn and a potential to score {player_turn.total_potential_loss}")




                # if not game.DEBUG:
                #     continuer = input("Continue ? y/n")
                # else:
                #     continuer = random.choice(['y', 'n'])

                player_turn.remaining_dice -= 1

        player_1.winner = True


main()
