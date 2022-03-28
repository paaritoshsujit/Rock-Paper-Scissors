
########################################################################################
##### Implementing a game of Rock, Paper, Scissors, where a user plays against CPU  ####
########################################################################################

import random

def play_rps():
    user = input(" What's your choice? 'r' for rock, 'p' for paper, 's' for scissors  : ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Draw!'
    if is_win(user, computer):
        return 'You Win!'
    
    return 'You Lose!'
    


def is_win(player, opponent):

    if (player== 'r' and opponent == 's') or (player== 'p' and opponent == 'r') or (player== 's' and opponent == 'p'):
        return True

print(play_rps())