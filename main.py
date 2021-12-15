import function
from operator import itemgetter, attrgetter
player_dict, roll_dict = function.set_player()
turn = 1
we_have_a_winner = False
while we_have_a_winner == False:
    for player_name, player_score in player_dict.items():
        player_score_list = player_dict.values()
        rank_list = sorted(list(player_score_list), key=None, reverse=True)
        player_turn_score = 0
        dice_to_roll = function.DEFAULT_DICES_NB
        print('\nturn #' + str(turn) + '--> ' + str(player_name) +' rank # ' + str(rank_list.index(player_score) + 1) + ', ' + 'score ' + str(player_score) + ' \n')
        roll = 1
        while dice_to_roll > 0:
            player_roll_score = 0
            dice_set = function.roll_dice_set(dice_to_roll)
            player_roll_score, total_winning_dice, dice_to_roll, player_winning_list = function.analyse_score(dice_set,dice_to_roll)
            player_turn_score += player_roll_score
            print('roll #' + str(roll) + ' : ' + str(total_winning_dice) + ' scoring dices ' + str(player_winning_list) + ' scoring ' + str(player_roll_score) + ', ' + 'potential turns score ' + str(player_turn_score) + ', ' + 'remaining dice to roll : ' + str(dice_to_roll))
            if total_winning_dice == 0:
                print('you lose this turn and a potential to score ' + str(player_turn_score))
                dice_to_roll = 0
            else:
                user_answer = input('do you want to roll again ? y/n ')
                if user_answer == 'n':
                    player_dict[player_name]+= player_turn_score
                    print('\n'+ player_name + ' win this turn, scoring ' + str(player_turn_score) + '\n')
                    dice_to_roll = 0
                    if player_dict[player_name] >= function.DEFAULT_TARGET_SCORE:
                        we_have_a_winner= True
                        function.analyse_game(player_dict, player_name, turn)
            roll += 1
            roll_dict[player_name] += 1

    for player_name, player_score in sorted(player_dict.items(), key=lambda x: x[1], reverse=True):
        print(player_name + ' --> ' + str(player_score))
    if player_dict[player_name] >= function.DEFAULT_TARGET_SCORE:
        we_have_a_winner= True
        function.analyse_game(player_dict, player_name, turn)
    turn += 1
