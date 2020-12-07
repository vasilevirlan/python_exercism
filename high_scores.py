# Manage a game player's High Score list.

# Your task is to build a high-score component of the classic Frogger game, one
# of the highest selling and addictive games of all time, and a classic of the 
# arcade era. Your task is to write methods that return the highest score from 
# the list, the last added score and the three highest scores.


def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return sorted(scores, reverse=True)[0:3]
