import random

## CONFIG PARTIE
# Nombre de tours réalisés
TURNS = 0
# Score à atteindre
DEFAULT_TARGET_SCORE = 2000
# Nombre de faces des dés
NB_DICE_FACES = 6
# Nombre de dés jetés
NB_DICE_ROLLS = 3
# Chiffres gagnants du dés
LIST_SCORING_DICE_VALUE = [1, 5]
# Points associés aux chiffres gagnants du dés
LIST_SCORING_MULTIPLIER = [100, 50]
# Nombre d'occurences pour déclencher le bonus
TRIGGER_OCCURRENCE_FOR_BONUS = 3
# Multiplicateur de points pour un bonus classique
BONUS_VALUE_FOR_NORMAL_BONUS = 100
# Multiplicateur de points pour un ACE
BONUS_VALUE_FOR_ACE_BONUS = 1000
# Booléen gagnant
WINNER = False
# Debug
DEBUG = True


## JOUEURS
# Liste des joueurs
PLAYERS = ["Romain", "François", "Stéphane", "Laurent", "Christophe", "Isabelle", "Sylvie"]
# Scores des joueurs
SCORES = [0] * len(PLAYERS)
# Dés restants des joueurs
REMAINING = [NB_DICE_ROLLS] * len(PLAYERS)

## STATS
# Tours joués de chaque joueurs
STAT_TOTAL_ROLLS = [0] * len(PLAYERS)
# Bonus gagnés de chaque joueurs
STAT_TOTAL_BONUS = [0] * len(PLAYERS)
# Pertes de points de chaque joueurs
STAT_TOTAL_POTENTIAL_LOSS = [0] * len(PLAYERS)
# Score maximum réalisé dans un tour par un joueur
STAT_MAX_TURN_SCORING = ["", 0]
# Liste des lancés scorants
STAT_SCORING_TURNS = []
# Liste des lancés non scorants
STAT_NON_SCORING_TURNS = []


def roll_dice_set(nb_dice_rolls):
    rolls = [0] * NB_DICE_FACES
    for i in range(nb_dice_rolls):
        index = random.randint(1, NB_DICE_FACES)
        rolls[index - 1] += 1
    return rolls


def calculateBonus(rolls, playerRemaining, usedRemainings):
    endWhile = 0
    points = 0
    scoringDices = 0
    scoringDicesTotal = 0
    while endWhile == 0:
        endWhile = 1
        for i in range(NB_DICE_FACES):
            if rolls[i] >= TRIGGER_OCCURRENCE_FOR_BONUS:
                multiplicateur = i + 1
                points += BONUS_VALUE_FOR_NORMAL_BONUS * multiplicateur
                rolls[i] -= TRIGGER_OCCURRENCE_FOR_BONUS
                endWhile = 0
                scoringDicesTotal += TRIGGER_OCCURRENCE_FOR_BONUS
                if i not in usedRemainings:
                    scoringDices += 1
                    usedRemainings.append(i)

    return rolls, points, playerRemaining-scoringDices, scoringDicesTotal


def calculatePoints(rolls, points, playerRemaining, usedRemainings):
    endWhile = 0
    scoringDices = 0
    scoringDicesTotal = 0
    while endWhile == 0:
        endWhile = 1
        for i in range(NB_DICE_FACES):
            if rolls[i] > 0 and i + 1 in LIST_SCORING_DICE_VALUE:
                points += LIST_SCORING_MULTIPLIER[LIST_SCORING_DICE_VALUE.index(i + 1)]
                rolls[i] -= 1
                endWhile = 0
                scoringDicesTotal += 1
                if i not in usedRemainings:
                    scoringDices += 1
                    usedRemainings.append(i)

    return points, rolls, playerRemaining-scoringDices, scoringDicesTotal


while not WINNER:
    TURNS += 1
    i = 0
    REMAINING = [NB_DICE_ROLLS] * len(PLAYERS)
    for i in range(len(PLAYERS)):
        print("\nTurn #" + str(TURNS) + " --> " + PLAYERS[i] + " score: " + str(SCORES[i]))
        continuer = 'y'
        rollNumber = 1
        potentialScore = 0
        usedRemainings = []
        scoringDices = 0
        scoringDicesTotal = 0
        while REMAINING[i] > 0 and continuer == 'y':
            myRolls = roll_dice_set(REMAINING[i])
            print(myRolls)
            myRolls, myPoints, REMAINING[i], scoringDicesTotal = calculateBonus(myRolls, REMAINING[i], usedRemainings)
            myPoints, myRolls, REMAINING[i], scoringDicesTotal2 = calculatePoints(myRolls, myPoints, REMAINING[i], usedRemainings)

            scoringDicesTotal += scoringDicesTotal2
            STAT_TOTAL_BONUS[i] += scoringDicesTotal2

            potentialScore += myPoints
            print("Roll #" + str(rollNumber) + " : " + str(scoringDicesTotal) + " scoring dices, scoring " + str(myPoints) + " pts, potential total turn score " + str(
                SCORES[i] + potentialScore) + " pts, remaining dice to roll : " + str(REMAINING[i]))

            continuer = 'n'
            if REMAINING[i] > 0 and myPoints > 0:
                if not DEBUG:
                    continuer = input("Continue ? y/n")
                else:
                    continuer = random.choice(['y', 'n'])
            elif REMAINING[i] == 0 and myPoints > 0:
                print("=> You win this turn, scoring " + str(potentialScore) + " pts")
                STAT_SCORING_TURNS.append(potentialScore)
                if potentialScore > STAT_MAX_TURN_SCORING[1]:
                    STAT_MAX_TURN_SCORING[1] = potentialScore
                    STAT_MAX_TURN_SCORING[0] = PLAYERS[i]
                SCORES[i] += potentialScore
            else:
                print("=> You lose this turn and a potential to score " + str(potentialScore) + " pts")
                STAT_NON_SCORING_TURNS.append(potentialScore)
                STAT_TOTAL_POTENTIAL_LOSS[i] += potentialScore
                potentialScore = 0
                continuer = 'n'

            rollNumber += 1

        STAT_TOTAL_ROLLS[i] += rollNumber

        if potentialScore > 0:
            print("=> You win this turn, scoring " + str(potentialScore) + " pts")
            STAT_SCORING_TURNS.append(potentialScore)
            if potentialScore > STAT_MAX_TURN_SCORING[1]:
                STAT_MAX_TURN_SCORING[1] = potentialScore
                STAT_MAX_TURN_SCORING[0] = PLAYERS[i]
            SCORES[i] += potentialScore

        if SCORES[i] > DEFAULT_TARGET_SCORE:
            WINNER = i
            break

        totalScores = "Total scores :"
        for n in range(len(PLAYERS)):
            totalScores += " " + PLAYERS[n] + " --> " + str(SCORES[n]) + " "
        print(totalScores)

# On affiches les différents statistiques de la partie
print("Game in " + str(TURNS) + " turns")
for i in range(len(PLAYERS)):
    if WINNER == i:
        print(PLAYERS[i] + " win ! scoring " + str(SCORES[i]) + " pts in " + str(STAT_TOTAL_ROLLS[i]) + " rolls, " + str(STAT_TOTAL_BONUS[i]) + " bonus and potential " + str(STAT_TOTAL_POTENTIAL_LOSS[i]) + " pts lost" )
    else:
        print(PLAYERS[i] + " lose ! scoring " + str(SCORES[i]) + " pts in " + str(STAT_TOTAL_ROLLS[i]) + " rolls, " + str(STAT_TOTAL_BONUS[i]) + " bonus and potential " + str(STAT_TOTAL_POTENTIAL_LOSS[i]) + " pts lost")


print("\nMax turn scoring : " + str(STAT_MAX_TURN_SCORING[0]) + " with " + str(STAT_MAX_TURN_SCORING[1]) + " pts")
print("Longest turn : " + str(PLAYERS[STAT_TOTAL_ROLLS.index(max(STAT_TOTAL_ROLLS))]) + " with " + str(max(STAT_TOTAL_ROLLS)) + " rolls")
print("Max turn loss : " + str(PLAYERS[STAT_TOTAL_POTENTIAL_LOSS.index(max(STAT_TOTAL_POTENTIAL_LOSS))]) + " with " + str(max(STAT_TOTAL_POTENTIAL_LOSS)) + " pts")

print("\nMean scoring turn : " + str(round(sum(STAT_SCORING_TURNS) / len(STAT_SCORING_TURNS), 2)) + " (" + str(len(STAT_SCORING_TURNS)) + " turns)")
print("Mean non scoring turn : " + str(round(sum(STAT_NON_SCORING_TURNS) / len(STAT_NON_SCORING_TURNS), 2)) + " (" + str(len(STAT_NON_SCORING_TURNS)) + " turns)")