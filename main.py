import function
players_list, player_score_list = function.set_player()
turn_stat_dict = {'max_turn_scoring':[0,''], 'longest_turn' : [0,''], 'max_turn_loss' : [0,'']}
total_turn = 0
loosing_turn = 0

turn = 1
we_have_a_winner = False
while we_have_a_winner == False:
    for player in players_list:
        total_turn += 1
        player_turn_score = 0
        dice_to_roll = function.DEFAULT_DICES_NB
        print('\nturn #' + str(turn) + '--> ' + str(player['name']) + ' rank # ' + str(
            player_score_list.index(player['score']) + 1) + ', ' + 'score ' + str(player['score']) + ' \n')
        roll = 1
        while dice_to_roll > 0:
            player_roll_score = 0
            dice_set = function.roll_dice_set(dice_to_roll)
            player_roll_score, total_winning_dice, dice_to_roll, player_winning_list, player['bonus'] = function.analyse_score(
                dice_set, dice_to_roll, player['bonus'])
            player_turn_score += player_roll_score
            if player_turn_score >= turn_stat_dict['max_turn_scoring'][0]:
                turn_stat_dict['max_turn_scoring'][0] = player_turn_score
                turn_stat_dict['max_turn_scoring'][1] = player['name']
            if total_winning_dice == function.DEFAULT_DICES_NB:
                dice_to_roll = function.DEFAULT_DICES_NB
                player['full-roll'] += 1
            if total_winning_dice > 0 and dice_to_roll == 0:
                dice_to_roll = function.DEFAULT_DICES_NB
                player['full-roll'] += 1
            print('roll #' + str(roll) + ' : ' + str(total_winning_dice) + ' scoring dices ' + str(player_winning_list) + ' scoring ' +
                  str(player_roll_score) + ', ' + 'potential turns score ' + str(player_turn_score) + ', ' + 'remaining dice to roll : ' + str(dice_to_roll))
            if total_winning_dice == 0:
                loosing_turn += 1
                if player_turn_score > turn_stat_dict['max_turn_loss'][0]:
                    turn_stat_dict['max_turn_loss'][0] = player_turn_score
                    turn_stat_dict['max_turn_loss'][1] = player['name']
                player['potential lost'] += player_turn_score
                print('you lose this turn and a potential to score ' +
                      str(player_turn_score))
                dice_to_roll = 0
            else:
                user_answer = input('do you want to roll again ? y/n ')
                if user_answer == 'n':
                    if roll > turn_stat_dict['longest_turn'][0]:
                        turn_stat_dict['longest_turn'][0] = roll
                        turn_stat_dict['longest_turn'][1] = player['name']
                    player_score_list[player_score_list.index(player['score'])] += player_turn_score
                    player['score'] += player_turn_score
                    print(
                        '\n' + player['name'] + ' win this turn, scoring ' + str(player_turn_score) + '\n')
                    dice_to_roll = 0
            if player['score'] >= function.DEFAULT_TARGET_SCORE:
                we_have_a_winner = True
                function.player_stat_analyse(
                    players_list,player['name'], turn, turn_stat_dict, total_turn, loosing_turn)
                break
            roll += 1
            player['roll'] += 1
    if we_have_a_winner==False:
        for player in sorted(players_list, key=lambda x: x['score'], reverse=True):
            print(player['name'] + ' --> ' + str(player['score']))
    else:
        break
    turn += 1
