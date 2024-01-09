import random

def player_turn(dice):
    result = random.randint(1, dice)
    print(f'Player roller a {result}')
    return result

def scoring(p1, p2):
    global p1_score, p2_score
    if p1 > p2:
        print('player 1 win')
        p1_score += 1
    elif p2 > p1:
        print('player 2 win')
        p2_score += 1
    else:
        print('draw')


p1_score = 0
p2_score = 0
rounds = int(input('How mane rounds would you like to play? '))

for play_round in range(rounds):
    player_1 = player_turn(6)
    player_2 = player_turn(6)


    scoring(player_1, player_2)
    print(f'score: player 1: {p1_score} vs. Player 2 : {p2_score}')
