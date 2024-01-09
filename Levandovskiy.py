import random


def player_turn(dise):
    result=random.randint(1, dise)
    print(f'Player roller a {result}')
    return result

def scoring(p1, p2):
    global p1_score; p2_score
    if p1> p2:
        print("player_1 win")
    elif p1 < p2:
        print("player_2 win")
    else:
        print('drow')


p1_score = 0
p2_score = 0


rounds= int(input("how many rounds you want to game?"))


for game_turn in range(rounds):
    player_1 = player_turn(6)
    player_2 = player_turn(6)



    scoring(player_1, player_2)
    print(f'score: player_1: {p1_score} vs. player_2: {p2_score}')
