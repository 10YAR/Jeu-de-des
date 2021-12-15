import random

# Target total score to win by default
DEFAULT_TARGET_SCORE = 2000

# Number of dices by default in the set
DEFAULT_DICES_NB = 5
# Number of side of the dices used in the game
NB_DICE_SIDE = 6

# List of dice value scoring
LIST_SCORING_DICE_VALUE = [1, 5]
# List of associated score for scoring dice values
LIST_SCORING_MULTIPLIER = [100, 50]

# Trigger for multiple bonus
TRIGGER_OCCURRENCE_FOR_BONUS = 3
# Special bonus multiplier for multiple ace bonus
BONUS_VALUE_FOR_ACE_BONUS = 1000
# Standard multiplier for multiple dices value bonus
BONUS_VALUE_FOR_NORMAL_BONUS = 100


def set_player():
    """Ask the number of player and their name and set the default rank and score

    Returns

    -------
    dict 
        a dictionnary of player and their score, with their name as key and their score as value
    dict
        a dictionnary of player and their number of roll in the game 
    """
    nb_player = int(input('How many player ?'))
    player_dict = {}
    roll_dict = {}
    for index in range(nb_player):
        player_name = input('Name of player ' + str(index+1) + ' ')
        player_dict[player_name] = 0
        roll_dict[player_name] = 0
    return player_dict, roll_dict


def roll_dice_set(nb_dice_to_roll):
    """Launch the dice and set a list with an occurence of each value return by the dice

    Parameters

    ----------
    nb_dice_to_roll : int
        the number of dice with have to roll, set at DEFAULT_SIDE_NB

    Returns

    -------
    list
        a list with all the occurence for each side dice

    """
    dice_value_occurrence_list = [0] * NB_DICE_SIDE
    for index in range(nb_dice_to_roll):
        dice_value = random.randint(1, NB_DICE_SIDE)
        dice_value_occurrence_list[dice_value-1] += 1
    return dice_value_occurrence_list


def analyse_bonus_score(dice_value_occurrence_list):
    """Analyse the if the player scored bonus points on his launch

    Parameters

    ----------
    dice_value_occurence_list: list
        list of all the occurence for each side of the dice which's appears on the player launch

    Returns

    -------
    list
       list of all the occurence for each side of the dice which's appears on the player launch minus those which's appears 3 times

    """
    score_bonus = 0
    bonus_winning_tuple = ()
    bonus_winning_tuple_list = []
    for side_value_index, dice_value_occurrence in enumerate(dice_value_occurrence_list):
        nb_of_bonus = dice_value_occurrence // TRIGGER_OCCURRENCE_FOR_BONUS
        if nb_of_bonus > 0:
            if side_value_index == 0:
                bonus_multiplier = BONUS_VALUE_FOR_ACE_BONUS
            else:
                bonus_multiplier = BONUS_VALUE_FOR_NORMAL_BONUS
            score_bonus += nb_of_bonus * \
                bonus_multiplier * (side_value_index + 1)
            bonus_winning_tuple = (
                TRIGGER_OCCURRENCE_FOR_BONUS, side_value_index+1)
            bonus_winning_tuple_list.append(bonus_winning_tuple)
            dice_value_occurrence_list[side_value_index] %= TRIGGER_OCCURRENCE_FOR_BONUS
    return score_bonus, bonus_winning_tuple_list, dice_value_occurrence_list,


def analyse_standard_score(dice_value_occurrence_list):
    score_standard = 0
    standard_winning_tuple = ()
    standard_winning_tuple_list = []
    for scoring_value, scoring_multiplier in zip(LIST_SCORING_DICE_VALUE, LIST_SCORING_MULTIPLIER):
        score_standard += dice_value_occurrence_list[scoring_value -
                                                     1] * scoring_multiplier
        if dice_value_occurrence_list[scoring_value - 1] > 0:
            standard_winning_tuple = (
                dice_value_occurrence_list[scoring_value-1], scoring_value)
            standard_winning_tuple_list.append(standard_winning_tuple)
        dice_value_occurrence_list[scoring_value-1] = 0
    return score_standard, standard_winning_tuple_list, dice_value_occurrence_list,


def analyse_score(dice_value_occurence_list, nb_dice_to_roll):
    bonus_score, bonus_winning_tuple_list, dice_value_occurence_list, = analyse_bonus_score(
        dice_value_occurence_list)
    standard_score, standard_winning_tuple_list, dice_value_occurence_list, = analyse_standard_score(
        dice_value_occurence_list)
    nb_winning_dice = nb_dice_to_roll - sum(dice_value_occurence_list)
    if nb_winning_dice > 0:
        nb_dice_to_roll = sum(dice_value_occurence_list)
    else:
        nb_dice_to_roll = 0
    if not bonus_winning_tuple_list:
        return bonus_score + standard_score, nb_winning_dice, nb_dice_to_roll, standard_winning_tuple_list
    elif not standard_winning_tuple_list:
        return bonus_score + standard_score, nb_winning_dice, nb_dice_to_roll, bonus_winning_tuple_list
    elif not standard_winning_tuple_list and not bonus_winning_tuple_list:
        return bonus_score + standard_score, nb_winning_dice, nb_dice_to_roll, bonus_winning_tuple_list
    else:
        for bonus_tuple_value, standard_tuple_value in zip(bonus_winning_tuple_list, standard_winning_tuple_list):
            winning_tuple_list = []
            winning_tuple_list.append(standard_tuple_value)
            winning_tuple_list.append(bonus_tuple_value)
        return bonus_score + standard_score, nb_winning_dice, nb_dice_to_roll, winning_tuple_list


def analyse_game(player_dict, winner_name, turn, roll_dict):
    player_dict_key_list = list(player_dict)
    player_dict_values = player_dict.values()
    roll_dict_values = player_dict.values()
    roll_dict_values_list = list(roll_dict_values)
    player_dict_values_list = list(player_dict_values)
    winner_score = player_dict_values_list.pop(player_dict_key_list.index(winner_name))
    winner_name = player_dict_key_list.pop(player_dict_key_list.index(winner_name))
    winner_roll = roll_dict_values_list.pop(player_dict_key_list.index(winner_name))
    print('{} win ! scoring  {} in {} roll'
        .format(winner_name,winner_score, winner_roll)
    )
    if len(player_dict_key_list) >= 1:
        print('\nGame in %s turns' %(turn))
        for index in range(len(player_dict_key_list)):
            print('{} lose ! scoring {} in {} roll' 
                .format(player_dict_key_list[index], player_dict_values_list[index], roll_dict_values_list[index])
            )
