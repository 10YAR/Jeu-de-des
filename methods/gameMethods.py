from methods import statsMethods, scoreMethods, rollMethods, playerMethods
import gameConfig, utils

def play(turn_stat_dict, total_turn, turn, loosing_turn):
    we_have_a_winner = False
    players_list, player_score_list = playerMethods.set_player()
    while we_have_a_winner == False:
        for player in players_list:
            total_turn += 1
            player_turn_score = 0
            dice_to_roll = gameConfig.DEFAULT_DICES_NB
            utils.turn_print(player_score_list, turn, player)
            roll = 1
            while dice_to_roll > 0:
                player_roll_score = 0
                dice_set = rollMethods.roll_dice_set(dice_to_roll)
                player_roll_score, total_winning_dice, dice_to_roll, player_winning_list, player['bonus'] = scoreMethods.analyse_score(dice_set, dice_to_roll, player['bonus'])
                player_turn_score += player_roll_score
                statsMethods.max_scoring_turn_analyse(turn_stat_dict, player_turn_score,player)
                dice_to_roll, loosing_turn = rollMethods.roll(total_winning_dice, player, loosing_turn, player_turn_score, turn_stat_dict, dice_to_roll)
                utils.roll_print(roll, total_winning_dice, player_winning_list, player_roll_score, player_turn_score, dice_to_roll)
                if dice_to_roll > 0  and dice_to_roll <= gameConfig.DEFAULT_DICES_NB:
                    dice_to_roll = rollMethods.ask_new_roll(roll, turn_stat_dict, player_score_list, player_turn_score,player,dice_to_roll)
                we_have_a_winner = game_over(turn_stat_dict, players_list,turn, total_turn, loosing_turn, player)
                roll += 1
                player['roll'] += 1
        if we_have_a_winner==False:
            for player in sorted(players_list, key=lambda x: x['score'], reverse=True):
                utils.player_score_print(player)
        else:
            break
        turn += 1


def game_over(turn_stat_dict, players_list,turn, total_turn, loosing_turn, player):
    if player['score'] >= gameConfig.DEFAULT_TARGET_SCORE:
        statsMethods.player_stat_analyse(
        players_list,player['name'], turn, turn_stat_dict, total_turn, loosing_turn)
        return True
    return False