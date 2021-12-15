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
    players_list = []
    player_score_list = []
    for index in range(nb_player):
        player_dict = {}
        player_name = input('Name of player ' + str(index+1) + ' ')
        player_dict['name'] = player_name
        player_dict['score'] = 0
        player_dict['roll'] = 0
        player_dict['full-roll'] = 0
        player_dict['bonus'] = 0
        player_dict['potential lost'] = 0
        players_list.append(player_dict)
        player_score_list.append(player_dict['score'])
    return players_list, player_score_list


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
    """Analyse the bonus score, if the player scored bonus points on his launch

    Parameters

    ----------
    dice_value_occurence_list: list
        list of all the occurence for each side of the dice which's appears on the player launch

    Returns

    -------
    integer
        all the bonus point the player win with his roll
    list
        A list of all the tuple(number of winning dice, the winning side value) that make the player win bonus point.
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
    """Analyse the standard score if the player scored standard points on his launch

    Parameters

    ----------
    dice_value_occurence_list: list
        list of all the occurence for each side of the dice which's appears on the player launch

    Returns

    -------
    integer
        all the standard point the player win with his roll
    tuple
        A tuple of the number of winning dice and the winning side value  
    list
       list of all the occurence for each side of the dices which's appears on the player launch minus those which's give him standard points

    """
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

def handle_tuple_exception(bonus_winning_tuple_list,standard_winning_tuple_list, nb_dice_to_roll, dice_value_occurence_list, bonus_win_by_player ):
    """Handle the returns if the list receive by analyse_bonus_score() and analyse_standard_score() exist

    Parameters

    ----------
    bonus_winning_tuple_list : list
        A list of all the tuple(number of winning dice, the winning side value) that make the player win bonus point. 
    
    standard_winning_tuple_list : list
        A list of all the tuple(number of winning dice, the winning side value) that make the player win standard point.
    
    nb_dice_to_roll : integer
        The number of remaining dice to roll

    dice_value_occurence_list : list
        List of all the occurence for each side of the dice which's appears on the player launch minus those which's make him win
    
    bonus_win_by_player : integer
        Number of bonus the player win during the game
    
    Returns

    -------

    Integer
        number of dice winning
    Integer
        The number of remaining dice to roll
    List
        List of tuple(number of winning dice, the winning side value) 
    Integer
        Number of bonus the player win during the game 


    """
    nb_winning_dice = nb_dice_to_roll - sum(dice_value_occurence_list)
    if nb_winning_dice > 0:
        nb_dice_to_roll = sum(dice_value_occurence_list)
    elif nb_winning_dice == 5:
        nb_dice_to_roll =5
    else:
        nb_dice_to_roll = 0
    if not bonus_winning_tuple_list:
        return nb_winning_dice, nb_dice_to_roll, standard_winning_tuple_list,bonus_win_by_player
    elif not standard_winning_tuple_list:
        bonus_win_by_player += len(bonus_winning_tuple_list)
        return nb_winning_dice, nb_dice_to_roll, bonus_winning_tuple_list,bonus_win_by_player
    elif not standard_winning_tuple_list and not bonus_winning_tuple_list:
        return nb_winning_dice, nb_dice_to_roll, bonus_winning_tuple_list,bonus_win_by_player
    else:
        bonus_win_by_player += len(bonus_winning_tuple_list)
        for bonus_tuple_value, standard_tuple_value in zip(bonus_winning_tuple_list, standard_winning_tuple_list):
            winning_tuple_list = []
            winning_tuple_list.append(standard_tuple_value)
            winning_tuple_list.append(bonus_tuple_value)
        return nb_winning_dice, nb_dice_to_roll, winning_tuple_list,bonus_win_by_player

def analyse_score(dice_value_occurence_list, nb_dice_to_roll, bonus_win_by_player):
    """Analyse if the player scored and his total score

    Parameters

    ----------
    dice_value_occurence_list: list
        list of all the occurence for each side of the dice which's appears on the player launch

    Returns

    -------
    integer
        the total point the player win with his roll
    tuple
        A tuple of the number of winning dice and the winning side value  
    list
       list of all the occurence that did not give him point

    """
    bonus_score, bonus_winning_tuple_list, dice_value_occurence_list, = analyse_bonus_score(
        dice_value_occurence_list)
    standard_score, standard_winning_tuple_list, dice_value_occurence_list, = analyse_standard_score(
        dice_value_occurence_list)  
    nb_winning_dice, nb_dice_to_roll, winning_tuple_list,bonus_win_by_player = handle_tuple_exception(bonus_winning_tuple_list,standard_winning_tuple_list, nb_dice_to_roll,dice_value_occurence_list, bonus_win_by_player)
    return  bonus_score + standard_score,nb_winning_dice, nb_dice_to_roll, winning_tuple_list,bonus_win_by_player
    


def player_stat_analyse(players_list, winner_name, turn, turn_stat_dict, total_turn, loosing_turn):
    total_score = 0
    total_potential_lost = 0
    scoring_turn = total_turn - loosing_turn
    print('\nGame in %s turns' %(turn))
    players_list_sorted_by_score = sorted(players_list, key=lambda x: x['score'], reverse=True)
    for player in players_list_sorted_by_score:
        total_score += player['score']
        total_potential_lost += player['potential lost']
        if player['name'] == winner_name:
            print('{} win ! scoring  {} in {} roll with {} full roll, {} bonus and {} potential points lost'
                .format(player['name'],player['score'],player['roll'], player['full-roll'], player['bonus'],player['potential lost'] )
            )
        else: 
            print('{} loose ! scoring  {} in {} roll with {} full roll, {} bonus and {} potential points lost'
                .format(player['name'],player['score'],player['roll'], player['full-roll'], player['bonus'],player['potential lost'] )
            )
    turn_stat_analyse(turn_stat_dict)
    mean_scoring_turn = round(total_score/scoring_turn,2)
    mean_non_scoring_turn = round(total_potential_lost/loosing_turn,2)
    print('\nMean scoring turn : {} ({} turns)\nMean non scoring turn : {} ({} turns)'
        .format(mean_scoring_turn,scoring_turn, mean_non_scoring_turn, loosing_turn)
    )


def turn_stat_analyse(turn_stat_dict):
    print('\nMax turn scoring : {} with {} \nLongest turn : {} with {} roll \nMax turn loss : {} with {}'
        .format(turn_stat_dict['max_turn_scoring'][1],turn_stat_dict['max_turn_scoring'][0],turn_stat_dict['longest_turn'][1], turn_stat_dict['longest_turn'][0], turn_stat_dict['max_turn_loss'][1], turn_stat_dict['max_turn_loss'][0]  )
    )